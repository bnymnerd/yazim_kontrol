import re
from yazim_kontrol import check_spelling

def get_text_from_file():
    # Dosyadan metin okuma işlemi
    try:
        with open("girdi.txt", "r") as file:
            text = file.read().strip()  # Dosyadaki metni okur
            if not text:
                print("girdi.txt dosyasında içerik bulunamadı!")
            return text
    except FileNotFoundError:
        print("girdi.txt dosyası bulunamadı!")
        return None
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        return None

def save_output(original_text, corrected_text):
    # Çıktılar.txt dosyasına kaydetme işlemi
    try:
        with open("ciktilar.txt", "a") as file:
            file.write(f"Orijinal Metin: {original_text}\n")
            file.write(f"Düzeltilmiş Metin: {corrected_text}\n\n")
    except Exception as e:
        print(f"Çıktı kaydedilirken hata oluştu: {e}")

def main():
    # Dosyadan metin alıyoruz
    text = get_text_from_file()
    if text is None:
        return  # Dosya okunamadıysa programdan çık

    # Geçersiz karakterler kontrolü (sayilar, semboller)
    invalid_pattern = re.compile(r'[0-9!@#$%^&*üöşğÜÖŞĞİı(),.?":{}|<>]')
    if invalid_pattern.search(text):
        print("Geçersiz karakterler tespit edildi: Sayılar veya semboller kullanılamaz.")
        return  # Geçersiz giriş yapıldığında metni işlemeden çık

    # Yazım hatalarını kontrol ediyoruz
    corrected_text = check_spelling(text)

    # Çıktıları dosyaya kaydediyoruz (sadece düzeltmeyi kaydedeceğiz)
    save_output(text, corrected_text)

if __name__ == "__main__":
    main()
