import pytest
import re


# Geçersiz içerik kontrolü için fonksiyon
def check_invalid_content(file_path):
    # Geçersiz içerik kontrolü için düzenli ifadeler (regex)
    invalid_pattern = re.compile(r'[0-9!@#$%^&*(),.?":{}|<>]')  # Sayılar ve semboller

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        invalid_lines = []
        for i, line in enumerate(lines):
            if invalid_pattern.search(line):  # Geçersiz bir karakter bulursa
                invalid_lines.append((i + 1, line.strip()))  # Satır numarasını ve metni ekler

        if invalid_lines:
            return invalid_lines  # Geçersiz içerik bulundu
        return None  # Geçerli içerik

    except Exception as e:
        return str(e)  # Hata durumunda mesaj döner


# Test: Geçersiz içerik kontrolü
def test_invalid_content():
    file_path = 'ciktilar.txt'

    # Geçersiz içerik kontrolü
    invalid_lines = check_invalid_content(file_path)

    if invalid_lines:
        pytest.fail(f"Geçersiz içerik bulundu: {invalid_lines}")  # Testi başarısız kıl, hata mesajı ile