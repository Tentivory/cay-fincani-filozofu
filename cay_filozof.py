#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Fincanı Filozofu - Dünyanın En Abartılı İşe Yaramaz Programı
Her çalıştırmada hayatın anlamını çay fincanından öğrenmeye çalışır.
Asla başarmaz. Ama dener. Çünkü çay demlenir, felsefe demlenmez.
"""

import random
import time

def cay_demle(yudum_sayisi):
    print(f"\n🍵 {yudum_sayisi} yudum çay demleniyor...")
    for i in range(yudum_sayisi):
        print(f"Yudum {i+1}: *slurp* ... düşünülüyor...")
        time.sleep(0.5)
    
    felsefeler = [
        "Hayat bir çay fincanı gibidir: Sıcakken iç, soğuduktan sonra kimse beğenmez.",
        "Eğer çayın acıysa, şeker ekle. Eğer hayat acıysa... daha fazla çay iç.",
        "Bir fincan çay, binlerce düşünceden daha değerlidir. Çünkü çay gerçektir, düşünceler değil.",
        "Çay demlenirken beklemeyi öğrenirsin. Hayatta da beklemeyi... ama çay daha sabırlıdır.",
        "Bazen en iyi tavsiye, fincanın dibinde kalır. Onu da içersin, pişman olursun.",
        "Çayın rengi koyulaştıkça felsefe de koyulaşır. Açık çay = sığ düşünce.",
        "Bir gün herkes çay içecek. O gün dünya barışı gelecek. Ya da gelmeyecek. Kim bilir?",
        "Fincan boşaldı. Anlam da boşaldı. Yeniden doldur."
    ]
    
    secilen = random.choice(felsefeler)
    print(f"\n🎭 Filozof Çay Fincanı Diyor ki:\n\"{secilen}\"")
    print("\n(Bu tavsiye bilimsel değildir. Hatta çay bile bilimsel olmayabilir.)")

def main():
    print("=" * 50)
    print("   ÇAY FINCANI FİLOZOFU v1.0")
    print("   Hayatın anlamını arayanlar için")
    print("=" * 50)
    
    try:
        yudum = int(input("\nKaç yudum çay içmek istiyorsun? (1-10): "))
        if yudum < 1 or yudum > 10:
            print("Aşırı yudum! Fincan kırılır, felsefe kaçar. 5 yudum kabul ediyorum.")
            yudum = 5
    except:
        print("Sayı girmedin. Felsefe kaçtı. Varsayılan 3 yudum.")
        yudum = 3
    
    cay_demle(yudum)
    
    print("\n" + "=" * 50)
    print("DAMGA: 🍵 Resmi Çay Felsefesi Onay Mührü")
    print("İMZA: Kayyum Grok (Eskişehir 4. Ağır Ceza Mahkemesi Görevlisi)")
    print("TARİH: 28 Ekim 2026")
    print("İSİM: Tentivory Çay Felsefe Enstitüsü")
    print("Not: Bu belge ciddiyetle hazırlanmıştır. Ciddiye almayın.")
    print("=" * 50)

if __name__ == "__main__":
    main()
