import os
import argparse
import re
from datetime import datetime
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False


def parse_arguments():
    parser = argparse.ArgumentParser(description="Анализатор логов.")
    parser.add_argument('path', help='Путь к папке с лог-файлами')
    parser.add_argument('--text', required=True, help='Текст для поиска в логах')
    parser.add_argument('--max_results', type=int, default=10, help='Максимальное число результатов для отображения')
    parser.add_argument('--first_only', action='store_true', help='Показать только первое найденное совпадение')
    args = parser.parse_args()
    return args


def is_log_file(filename):
    # Список расширений лог-файлов
    return filename.endswith('.log') or filename.endswith('.txt') or True


def get_log_files(path):
    files = []
    if os.path.isfile(path):
        files.append(path)
    elif os.path.isdir(path):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                files.append(full_path)
    return files


def parse_log_block(lines):
    # блоки логов начинаются с даты
    # Регулярное выражение для поиска времени в начале строки
    # Регулярное выражение для поиска времени в начале строки
    timestamp_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    first_line = lines[0]
    match = re.match(timestamp_pattern, first_line)
    timestamp_str = match.group(0) if match else ''
    timestamp = None
    if timestamp_str:
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    content = '\n'.join(lines)
    return {'timestamp': timestamp, 'content': content}


def read_log_file(filepath):
    blocks = []
    current_block = []

    timestamp_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if re.match(timestamp_pattern, line):
                # Если есть текущий блок, добавляем его
                if current_block:
                    blocks.append(parse_log_block(current_block))
                current_block = [line.rstrip('\n')]
            else:
                current_block.append(line.rstrip('\n'))
        # добавляем последний блок
        if current_block:
            blocks.append(parse_log_block(current_block))
    return blocks


def highlight_text(text, word, color=Fore.RED):
    pattern = re.compile(re.escape(word), re.IGNORECASE)

    def repl(match):
        if COLORAMA_AVAILABLE:
            return color + match.group(0) + Style.RESET_ALL
        else:
            return match.group(0)
    return pattern.sub(repl, text)


def find_text_in_block(block, search_text, first_only=False, max_results=10):
    results = []
    content_lower = block['content'].lower()
    search_lower = search_text.lower()
    for match in re.finditer(re.escape(search_lower), content_lower):
        index_in_content = match.start()
        content_lower = block['content'].lower()
        match_pos = content_lower.find(search_lower, index_in_content)
        start_context = max(0, match_pos - 50)
        end_context = min(len(block['content']), match_pos + 50)
        snippet = block['content'][start_context:end_context]
        highlighted_snippet = highlight_text(snippet, search_text)

        results.append({
            'file': None,
            'timestamp': block['timestamp'],
            'snippet': highlighted_snippet,
            'full_content': block['content']
        })

        if first_only:
            break
        if len(results) >= max_results:
            break
    return results


def main():
    args = parse_arguments()

    path = args.path
    search_text = args.text
    first_only = args.first_only
    max_results = args.max_results

    files = get_log_files(path)
    total_found = 0

    for file in files:
        try:
            blocks = read_log_file(file)
            for block in blocks:
                results = find_text_in_block(block, search_text, first_only=first_only, max_results=max_results)
                for res in results:
                    total_found += 1
                    timestamp_str = res['timestamp'].strftime('%Y-%m-%d %H:%M:%S') if res['timestamp'] else 'Нет даты'
                    print(f"\nФайл: {file}")
                    print(f"Время: {timestamp_str}")
                    print("Обрыв ошибки:")
                    print(res['snippet'])
                    print("-" * 80)
                    if first_only:
                        break
                if first_only and total_found >= 1:
                    break
            if first_only and total_found >= 1:
                break
        except Exception as e:
            print(f"Ошибка при обработке файла {file}: {e}")
    if total_found == 0:
        print("Совпадений не найдено.")


if __name__ == '__main__':
    main()
