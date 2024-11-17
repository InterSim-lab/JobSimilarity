# InterSim API

## Clone to your Local Machine

```bash
git clone htps://example.com
cd example
```

I recommend to make **Virtual Environment** before installing dependencies.

```bash
# Windows
pip install -r requirements.txt
# Or Linux
pip3 install -r requirements.txt
```

## Run the script

```bash
uvicorn app.main:app --reload
```

## API Documentation

### > Get Random Jobs

```bash
/api/jobs/random
```

Params:

limit (int): The number of random jobs to return. Defaults to 10.
Example:
```bash
/api/jobs/random?limit=20
```

#### Response:

```json
[
	{
    "id": 48,
    "title": "Field Operational Staff",
    "company": "PT. Sumber Prima Aneka Cemerlang",
    "category": "Operations",
    "status": "Full-Time · Hybrid",
    "min_edu": "Minimum Senior/Vocational High School",
    "min_exp": "Less than a year of experience",
    "description": "Job description for Field Operational Staff at PT. Sumber Prima Aneka CemerlangRingkasan Pekerjaan:Peran ini ideal untuk individu yang nyaman bekerja di lingkungan yang dinamis dan menikmati pekerjaan di luar kantor. Sebagai Staf Operasional Lapangan, Anda akan bertanggung jawab untuk melakukan survei lapangan di berbagai lokasi, menilai potensi peluang bisnis laundry dan mengumpulkan wawasan tentang pesaing. Hasil temuan Anda akan sangat penting dalam membentuk strategi bisnis kami.Tanggung Jawab Utama:Survei Lokasi dan Pesaing:Melakukan survei langsung di lokasi untuk mengevaluasi potensi tempat usaha.Mengamati dan mendokumentasikan aktivitas pesaing dan kehadiran pasar.Mengumpulkan wawasan tentang kondisi bisnis, demografi konsumen, dan potensi hambatan/tantangan.Pengumpulan Data dan Pelaporan:Mengumpulkan data dari lokasi yang disurvei dan menyusun temuan dalam laporan yang jelas dan akurat.Menyampaikan wawasan dan rekomendasi berdasarkan data lapangan untuk mendukung pengambilan keputusan.Menyediakan laporan lisan dan tulisan dari observasi dan memberikan saran.Komunikasi dengan Pemangku Kepentingan:Berkomunikasi secara efektif dengan anggota tim dan manajer mengenai temuan lapangan.Membangun hubungan baik dengan kontak terkait di lapangan.Menyampaikan temuan dan memberikan update dengan jelas dan profesional.Kerja Lapangan Dinamis:Melakukan kunjungan ke berbagai lokasi di area Jakarta dan sekitarnya.Fleksibel dan responsif terhadap perubahan jadwal dan penugasan lokasi.Menjalani peran yang membutuhkan aktivitas fisik dan perjalanan dalam wilayah.Kualifikasi:Pendidikan SMA/setara atau sarjana di bidang bisnis, pemasaran, atau bidang terkait lainnya.Pengalaman terbukti dalam pekerjaan lapangan, peran operasional, atau posisi terkait.Memiliki SIM C dan motor untuk mobilitas survei.Keterampilan komunikasi dan interpersonal yang kuat.Teliti dengan keterampilan organisasi yang sangat baik.Kemampuan bekerja mandiri dan mengatur waktu secara efektif.Kemampuan dalam alat pengumpulan data dasar dan pelaporan (Microsoft Excel, Google Sheets, dll.).Familiar dengan area Jakarta Barat dan sekitarnya adalah nilai tambah.Keahlian yang Diutamakan:Pengalaman di bidang bisnis laundry.Pengalaman dalam survei bisnis atau riset pasar.Pengetahuan dasar tentang analisis pesaing dan dinamika pasar.Memiliki kemampuan bahasa Inggris dasar.Read Less",
    "url": "https://glints.com/id/en/opportunities/jobs/field-operational-staff/711d5a05-c1f1-4dfe-9482-38ca89c7fe76?utm_referrer=explore&traceInfo=45b6989a-5a06-49a6-8d2f-ef549d176ce5"
  },
  
  .
  .

  {
	  "id": 85,
    "title": "Personal Assistan",
    "company": "Reformd Group",
    "category": "Operations",
    "status": "Full-Time · On-site",
    "min_edu": "Minimum Associate Degree",
    "min_exp": "",
    "description": "Job description for Personal Assistan at Reformd GroupRole DescriptionWe are seeking a full-time, on-site Personal Assistant to the Director at ReFormd Group, based in the Jakarta Metropolitan Area. The Personal Assistant will be responsible for providing executive administrative support, managing the director's calendar, assisting with general administrative tasks, and utilizing clerical skills to ensure the smooth operation of daily activities.Qualifications- 3 to 5 years of experience in a personal assistant or executive administrative role- Proficiency in diary/calendar management- Excellent organizational, time management, and administrative skills- Strong attention to detail and problem-solving abilities- Effective communication and interpersonal skills- Fluent in English (both spoken and written)- Ability to travel if required- Previous experience in a similar role is preferred- A Bachelor’s degree in Business Administration or a related field is a plusRead Less",
    "url": "https://glints.com/id/en/opportunities/jobs/personal-assistan/81df8f84-0a00-48b4-a580-3434f568ce6d?utm_referrer=explore&traceInfo=957533d6-1063-478f-8467-d1f7ebbb673d"
	}
]
```

### > Get Detail Jobs
```bash
/api/jobs/[id]
```
Params:

**id**: The ID of the job to find similar jobs for.

Example:
```bash
/api/jobs/85
```

#### Response:

```json
[
	{
		"id": 85,
    "title": "Personal Assistan",
    "company": "Reformd Group",
    "category": "Operations",
    "status": "Full-Time · On-site",
    "min_edu": "Minimum Associate Degree",
    "min_exp": "",
    "description": "Job description for Personal Assistan at Reformd GroupRole DescriptionWe are seeking a full-time, on-site Personal Assistant to the Director at ReFormd Group, based in the Jakarta Metropolitan Area. The Personal Assistant will be responsible for providing executive administrative support, managing the director's calendar, assisting with general administrative tasks, and utilizing clerical skills to ensure the smooth operation of daily activities.Qualifications- 3 to 5 years of experience in a personal assistant or executive administrative role- Proficiency in diary/calendar management- Excellent organizational, time management, and administrative skills- Strong attention to detail and problem-solving abilities- Effective communication and interpersonal skills- Fluent in English (both spoken and written)- Ability to travel if required- Previous experience in a similar role is preferred- A Bachelor’s degree in Business Administration or a related field is a plusRead Less",
    "url": "https://glints.com/id/en/opportunities/jobs/personal-assistan/81df8f84-0a00-48b4-a580-3434f568ce6d?utm_referrer=explore&traceInfo=957533d6-1063-478f-8467-d1f7ebbb673d"
	}
]
```

### > GET Jobs by Category
```bash
/api/jobs/category/[category_name]
```

Params:

- **category**: The category of jobs to return.
- **limit**: The number of jobs to return. **Defaults to 10.**

Example: 
```bash
/api/jobs/category/Operations
```
```bash
/api/jobs/category/Operations?limit=15
```

#### Response:

```json
[
	{
    "id": 48,
    "title": "Field Operational Staff",
    "company": "PT. Sumber Prima Aneka Cemerlang",
    "category": "Operations",
    "status": "Full-Time · Hybrid",
    "min_edu": "Minimum Senior/Vocational High School",
    "min_exp": "Less than a year of experience",
    "description": "Job description for Field Operational Staff at PT. Sumber Prima Aneka CemerlangRingkasan Pekerjaan:Peran ini ideal untuk individu yang nyaman bekerja di lingkungan yang dinamis dan menikmati pekerjaan di luar kantor. Sebagai Staf Operasional Lapangan, Anda akan bertanggung jawab untuk melakukan survei lapangan di berbagai lokasi, menilai potensi peluang bisnis laundry dan mengumpulkan wawasan tentang pesaing. Hasil temuan Anda akan sangat penting dalam membentuk strategi bisnis kami.Tanggung Jawab Utama:Survei Lokasi dan Pesaing:Melakukan survei langsung di lokasi untuk mengevaluasi potensi tempat usaha.Mengamati dan mendokumentasikan aktivitas pesaing dan kehadiran pasar.Mengumpulkan wawasan tentang kondisi bisnis, demografi konsumen, dan potensi hambatan/tantangan.Pengumpulan Data dan Pelaporan:Mengumpulkan data dari lokasi yang disurvei dan menyusun temuan dalam laporan yang jelas dan akurat.Menyampaikan wawasan dan rekomendasi berdasarkan data lapangan untuk mendukung pengambilan keputusan.Menyediakan laporan lisan dan tulisan dari observasi dan memberikan saran.Komunikasi dengan Pemangku Kepentingan:Berkomunikasi secara efektif dengan anggota tim dan manajer mengenai temuan lapangan.Membangun hubungan baik dengan kontak terkait di lapangan.Menyampaikan temuan dan memberikan update dengan jelas dan profesional.Kerja Lapangan Dinamis:Melakukan kunjungan ke berbagai lokasi di area Jakarta dan sekitarnya.Fleksibel dan responsif terhadap perubahan jadwal dan penugasan lokasi.Menjalani peran yang membutuhkan aktivitas fisik dan perjalanan dalam wilayah.Kualifikasi:Pendidikan SMA/setara atau sarjana di bidang bisnis, pemasaran, atau bidang terkait lainnya.Pengalaman terbukti dalam pekerjaan lapangan, peran operasional, atau posisi terkait.Memiliki SIM C dan motor untuk mobilitas survei.Keterampilan komunikasi dan interpersonal yang kuat.Teliti dengan keterampilan organisasi yang sangat baik.Kemampuan bekerja mandiri dan mengatur waktu secara efektif.Kemampuan dalam alat pengumpulan data dasar dan pelaporan (Microsoft Excel, Google Sheets, dll.).Familiar dengan area Jakarta Barat dan sekitarnya adalah nilai tambah.Keahlian yang Diutamakan:Pengalaman di bidang bisnis laundry.Pengalaman dalam survei bisnis atau riset pasar.Pengetahuan dasar tentang analisis pesaing dan dinamika pasar.Memiliki kemampuan bahasa Inggris dasar.Read Less",
    "url": "https://glints.com/id/en/opportunities/jobs/field-operational-staff/711d5a05-c1f1-4dfe-9482-38ca89c7fe76?utm_referrer=explore&traceInfo=45b6989a-5a06-49a6-8d2f-ef549d176ce5"
  },
  
  .
  .

  {
	  "id": 85,
    "title": "Personal Assistan",
    "company": "Reformd Group",
    "category": "Operations",
    "status": "Full-Time · On-site",
    "min_edu": "Minimum Associate Degree",
    "min_exp": "",
    "description": "Job description for Personal Assistan at Reformd GroupRole DescriptionWe are seeking a full-time, on-site Personal Assistant to the Director at ReFormd Group, based in the Jakarta Metropolitan Area. The Personal Assistant will be responsible for providing executive administrative support, managing the director's calendar, assisting with general administrative tasks, and utilizing clerical skills to ensure the smooth operation of daily activities.Qualifications- 3 to 5 years of experience in a personal assistant or executive administrative role- Proficiency in diary/calendar management- Excellent organizational, time management, and administrative skills- Strong attention to detail and problem-solving abilities- Effective communication and interpersonal skills- Fluent in English (both spoken and written)- Ability to travel if required- Previous experience in a similar role is preferred- A Bachelor’s degree in Business Administration or a related field is a plusRead Less",
    "url": "https://glints.com/id/en/opportunities/jobs/personal-assistan/81df8f84-0a00-48b4-a580-3434f568ce6d?utm_referrer=explore&traceInfo=957533d6-1063-478f-8467-d1f7ebbb673d"
	}
]
```

### > GET Jobs Similar by **id**
```bash
/api/jobs/[id]/similar
```

Params:

- **id**: The ID of the job to find similar jobs for.
- **limit:** The number of jobs to return. **Defaults to 10.**

Example: 
```bash
/api/jobs/85/similar
```
Example: 
```bash
/api/jobs/85/similar?limit=20
```

#### Response:

```json
[
	{
	  "id": 85,
    "title": "Personal Assistan",
    "company": "Reformd Group",
    "category": "Operations",
    "status": "Full-Time · On-site",
    "min_edu": "Minimum Associate Degree",
    "min_exp": "",
    "description": "Job description for Personal Assistan at Reformd GroupRole DescriptionWe are seeking a full-time, on-site Personal Assistant to the Director at ReFormd Group, based in the Jakarta Metropolitan Area. The Personal Assistant will be responsible for providing executive administrative support, managing the director's calendar, assisting with general administrative tasks, and utilizing clerical skills to ensure the smooth operation of daily activities.Qualifications- 3 to 5 years of experience in a personal assistant or executive administrative role- Proficiency in diary/calendar management- Excellent organizational, time management, and administrative skills- Strong attention to detail and problem-solving abilities- Effective communication and interpersonal skills- Fluent in English (both spoken and written)- Ability to travel if required- Previous experience in a similar role is preferred- A Bachelor’s degree in Business Administration or a related field is a plusRead Less",
    "url": "https://glints.com/id/en/opportunities/jobs/personal-assistan/81df8f84-0a00-48b4-a580-3434f568ce6d?utm_referrer=explore&traceInfo=957533d6-1063-478f-8467-d1f7ebbb673d"
	}
	{
    "id": 48,
    "title": "Field Operational Staff",
    "company": "PT. Sumber Prima Aneka Cemerlang",
    "category": "Operations",
    "status": "Full-Time · Hybrid",
    "min_edu": "Minimum Senior/Vocational High School",
    "min_exp": "Less than a year of experience",
    "description": "Job description for Field Operational Staff at PT. Sumber Prima Aneka CemerlangRingkasan Pekerjaan:Peran ini ideal untuk individu yang nyaman bekerja di lingkungan yang dinamis dan menikmati pekerjaan di luar kantor. Sebagai Staf Operasional Lapangan, Anda akan bertanggung jawab untuk melakukan survei lapangan di berbagai lokasi, menilai potensi peluang bisnis laundry dan mengumpulkan wawasan tentang pesaing. Hasil temuan Anda akan sangat penting dalam membentuk strategi bisnis kami.Tanggung Jawab Utama:Survei Lokasi dan Pesaing:Melakukan survei langsung di lokasi untuk mengevaluasi potensi tempat usaha.Mengamati dan mendokumentasikan aktivitas pesaing dan kehadiran pasar.Mengumpulkan wawasan tentang kondisi bisnis, demografi konsumen, dan potensi hambatan/tantangan.Pengumpulan Data dan Pelaporan:Mengumpulkan data dari lokasi yang disurvei dan menyusun temuan dalam laporan yang jelas dan akurat.Menyampaikan wawasan dan rekomendasi berdasarkan data lapangan untuk mendukung pengambilan keputusan.Menyediakan laporan lisan dan tulisan dari observasi dan memberikan saran.Komunikasi dengan Pemangku Kepentingan:Berkomunikasi secara efektif dengan anggota tim dan manajer mengenai temuan lapangan.Membangun hubungan baik dengan kontak terkait di lapangan.Menyampaikan temuan dan memberikan update dengan jelas dan profesional.Kerja Lapangan Dinamis:Melakukan kunjungan ke berbagai lokasi di area Jakarta dan sekitarnya.Fleksibel dan responsif terhadap perubahan jadwal dan penugasan lokasi.Menjalani peran yang membutuhkan aktivitas fisik dan perjalanan dalam wilayah.Kualifikasi:Pendidikan SMA/setara atau sarjana di bidang bisnis, pemasaran, atau bidang terkait lainnya.Pengalaman terbukti dalam pekerjaan lapangan, peran operasional, atau posisi terkait.Memiliki SIM C dan motor untuk mobilitas survei.Keterampilan komunikasi dan interpersonal yang kuat.Teliti dengan keterampilan organisasi yang sangat baik.Kemampuan bekerja mandiri dan mengatur waktu secara efektif.Kemampuan dalam alat pengumpulan data dasar dan pelaporan (Microsoft Excel, Google Sheets, dll.).Familiar dengan area Jakarta Barat dan sekitarnya adalah nilai tambah.Keahlian yang Diutamakan:Pengalaman di bidang bisnis laundry.Pengalaman dalam survei bisnis atau riset pasar.Pengetahuan dasar tentang analisis pesaing dan dinamika pasar.Memiliki kemampuan bahasa Inggris dasar.Read Less",
    "url": "https://glints.com/id/en/opportunities/jobs/field-operational-staff/711d5a05-c1f1-4dfe-9482-38ca89c7fe76?utm_referrer=explore&traceInfo=45b6989a-5a06-49a6-8d2f-ef549d176ce5"
  },
  
  .
  .
]
```
