# irc-bootcamp-programming
Identitas : Aziziah Dina Nabilah Salma / Fisika 61 / GCS

#Resume Bootcamp Day 2
1. Pengenalan Divisi Programming. 
   Divisi programming adalah tim yang bertanggungjawab untuk memberi 'otak' kepada robot. Di IRC terbagi menjadi 3 divisi yakni programming VTOL, programming Transporter, dan GCS RP. Keterampilan teknis yang dibutuhkan yakni bahasa pemrograman, mikrokontroler, sensor & akuator, dan komunikasi.
2. Flowchart dan Pseudocode. 
   Flowchart merupakan representasi grafis proses atau algoritma dengan simbol standar untuk menggambar alur langkah-langkah. Sedangkan Pseudocode adalah penulisan algoritma dalam deskripsi yang mudah dipahami tanpa terikat sintaks tertentu.
3. Tipe data dan Variabel.
a. Variabel di Arduino (C/C++).
  Tipe Data Harus dideklarasikan sebelum digunakan (int, float, char, dll). Deklarasinya berupa int ledPin = 13. Skopnya Bisa global atau lokal. dan Sintaks lebih ketat dan memerlukan tipe data eksplisit.
b. Variabel di Python. 
Tipe data ditentukan otomatis (int, float, str, dll). Deklarasi berupa ledPin = 13. Skop Bisa global atau lokal. Dan Sintaks Lebih fleksibel dan sederhana.
4. Toolchain. 
   Toolchain yang digunakan yakni Arduino IDE, Platform IO, VS Code, Google Collab, PyCharm, WOKWI, Roboflow
5. Git dan Embedded System. 
   Git adalah sistem kontrol versi yang digunakan untuk mencatat perubahan pada file secara terstruktur dan terkelola, memungkinkan banyak orang bekerja pada proyek yang sama tanpa konflik.
   Embedded system adalah sistem komputer khusus yang dirancang untuk menjalankan tugas tertentu dalam perangkat yang lebih besar, dengan keterbatasan daya, memori, dan pemrosesan.

#Penjelasan camera_display.py
1. cv2.VideoCapture(0) membuka kamera default
2. cv2.putText() digunakan untuk menampilkan teks di layar
3. cv2.CascadeClassifier digunakan untuk mendeteksi wajah


#Penjelasan led_servo.ino
1. ledPin dan servoPin untuk LED dan servo
2. pinMode(ledPin, OUTPUT) mengatur pin LED sebagai output
3. Variabel previousMillis dan millis() digunakan agar LED berkedip tiap 1 detik tanpa menggunakan delay()
4. LED akan berubah status (nyala/mati) setiap 1000 milidetik
5. Servo digerakkan menggunakan myServo.write(angle) di dalam loop.
6. link wokwi :
