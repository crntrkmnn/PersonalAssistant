from Alarm import set_alarm
from Notes import add_note, list_notes, delete_note
from Appointments import add_appointment, list_appointments
from Tasks import add_task, list_tasks


def print_help():
    print("\nKullanım Talimatları:")
    print("Alarm Kurma: alarm kur HH:MM")
    print("Not Ekleme: not ekle: Not içeriği")
    print("Notları Listeleme: notlar")
    print("Not Silme: not sil ID")
    print("Randevu Ekleme: randevu ekle: Randevu içeriği")
    print("Randevuları Listeleme: randevular")
    print("Görev Ekleme: görev ekle: Görev içeriği")
    print("Görevleri Listeleme: görevler")
    print("Çıkış: exit\n")


def main():
    print_help()  # Kullanım talimatlarını başta göster

    while True:
        command = input("Komut girin: ").strip().lower()

        if command.startswith("alarm kur"):
            _, _, alarm_time_str = command.partition(" ")
            set_alarm(alarm_time_str)
        elif command.startswith("not ekle"):
            _, _, note_text = command.partition(": ")
            add_note(note_text.strip())
        elif command == "notlar":
            list_notes()
        elif command.startswith("not sil"):
            _, _, note_id_str = command.partition(" ")
            note_id_str = note_id_str.strip()  # ID'yi temizle
            if note_id_str.isdigit():
                note_id = int(note_id_str)
                delete_note(note_id)
            else:
                print("Geçersiz not ID'si. Lütfen geçerli bir sayı girin.")
        elif command.startswith("randevu ekle"):
            _, _, appointment_text = command.partition(": ")
            add_appointment(appointment_text.strip())
        elif command == "randevular":
            list_appointments()
        elif command.startswith("görev ekle"):
            _, _, task_text = command.partition(": ")
            add_task(task_text.strip())
        elif command == "görevler":
            list_tasks()
        elif command == "exit":
            break
        else:
            print("Geçersiz komut. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
