import cv2

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal mengambil frame")
        break

    # Tambahkan teks "Aziziah Dina"
    cv2.putText(
        frame, 
        "Aziziah Dina", 
        (50, 50), 
        cv2.FONT_TIMES_NEW_ROMAN, 
        1, 
        (0, 255, 0),  # Warna hijau (BGR)
        2, 
        cv2.LINE_AA
    )

    cv2.imshow("Kamera Aziziah Dina", frame)

    #Deteksi wajah
    cv2.CascadeClassifier

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
