import argparse
import os
import importlib.util

LABS_DIR = "labs"

def list_labs():
    """
    Вивести список доступних лабораторних робіт.
    """
    print("Доступні лабораторні роботи:")
    labs = sorted(os.listdir(LABS_DIR))
    for i, lab in enumerate(labs, start=1):
        readme_path = os.path.join(LABS_DIR, lab, "README.md")
        description = f"Лабораторна робота №{i}"
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                description = f.readline().strip()
        print(f"{i}. {lab} - {description}")

def run_lab(lab_number):
    """
    Запустити вказану лабораторну роботу.
    """
    labs = sorted(os.listdir(LABS_DIR))
    if lab_number < 1 or lab_number > len(labs):
        print(f"Помилка: Лабораторної роботи з номером {lab_number} не існує.")
        return

    lab_folder = labs[lab_number - 1]
    lab_path = os.path.join(LABS_DIR, lab_folder, f"{lab_folder}.py")

    if not os.path.exists(lab_path):
        print(f"Помилка: Файл {lab_path} не знайдено.")
        return

    # Завантаження та виконання файлу
    spec = importlib.util.spec_from_file_location("lab", lab_path)
    lab_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lab_module)

    if hasattr(lab_module, "main"):
        print(f"Запуск лабораторної роботи {lab_number}...")
        lab_module.main()
    else:
        print(f"Помилка: У файлі {lab_path} не знайдено функцію main.")

def main():
    """
    Основна функція CLI.
    """
    parser = argparse.ArgumentParser(description="CLI для роботи з лабораторними роботами.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Команда "list"
    subparsers.add_parser("list", help="Показати список доступних лабораторних робіт")

    # Команда "run"
    run_parser = subparsers.add_parser("run", help="Запустити лабораторну роботу")
    run_parser.add_argument("lab_number", type=int, help="Номер лабораторної роботи для запуску")

    args = parser.parse_args()

    if args.command == "list":
        list_labs()
    elif args.command == "run":
        run_lab(args.lab_number)

if __name__ == "__main__":
    main()
