import datetime
import time
import threading
from plyer import notification

def is_valid_time_format(time_str):
    if len(time_str) != 5 or time_str[2] != ':':
        return False
    try:
        hour, minute = map(int, time_str.split(':'))
        if 0 <= hour < 24 and 0 <= minute < 60:
            return True
    except ValueError:
        pass
    return False

def set_alarm(alarm_time_str):
    if not is_valid_time_format(alarm_time_str):
        print("Geçersiz zaman formatı. Lütfen 'HH:MM' formatında girin. Örnek: 08:30")
        return

    try:
        # Alarm zamanını belirle
        alarm_time = datetime.datetime.strptime(alarm_time_str, '%H:%M')
        now = datetime.datetime.now()
        alarm_time = alarm_time.replace(year=now.year, month=now.month, day=now.day)

        # Eğer alarm zamanı geçmişse, alarmı bir sonraki gün için ayarla
        if alarm_time < now:
            alarm_time += datetime.timedelta(days=1)

        # Zaman farkını hesapla
        time_diff = (alarm_time - now).total_seconds()

        print(f"Alarm kuruldu: {alarm_time.strftime('%H:%M')}. Süre: {time_diff} saniye.")

        # Alarm süresi geldiğinde bildirim gönder
        def alarm():
            time.sleep(time_diff)
            notification.notify(
                title='Alarm!',
                message=f"Alarm saati geldi: {alarm_time.strftime('%H:%M')}",
                timeout=10
            )

        # Alarmı ayrı bir iş parçacığında çalıştır
        threading.Thread(target=alarm).start()

    except ValueError:
        print("Geçersiz zaman formatı. Lütfen 'HH:MM' formatında girin. Örnek: 08:30")
