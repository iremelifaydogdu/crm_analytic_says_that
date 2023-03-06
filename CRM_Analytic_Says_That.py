#CRM Analitiği
#RFM Analizi
#Müşteri Yaşam Boyu Değeri
#Müşteri Yaşam Boyu Değeri Tahmini


#CRM Analitiğine Giriş
#CRM Nedir, CRM alanına girildiğinde bazı uygulamalar nelerdir, ve bunların CRM Analitiği ile ne ilişkisi vardır.
#CRM : Müşteri  İlişkileri Yönetimi
#Müşteri Yaşam Döngüsü Optimizasyonları : (customer lifecycle/journey/funnel) Müşterilerle kurulan iletişimin ya da etkileşimin görsel tekniklerle ifade edip bunları çeşitli KPI'larla takip edilebilir bir forma getirip takip etme imkanı sağlayan kavramlardır.
#(Görsel ve takip etme anlamında ifade eden döngülerdir.)
#KPI:Temel performans göstergeleri

#Müşteri İlişkisi Süreci'nde:
#İletişimin dili rengi olmalıdır. (dil, renk, görseller, kampanyalar)

#Müşteri edinme/bulma çalışmaları: Online ve offline kanaldan gerçekleştirilen çabaları ifade eder. Yeni müşteriler bulmaya çalışır.

#Pazarlama kanunları 101: Yeni müşteri bulma maliyeti > varolanı elde tutma

#Müşteri elde tutma (terk çalışmaları)


#Cross sell (çapraz satış)= Bir ürünün yanında yan ürün de satmak istemek,tamamlayıcı ürünlerin satışı
#Upsell (üst satış)=küçük boyutlu kola yerine büyük boyutlu kola satmak

#Müşteri Segmentasyon Çalışmaları:
#Bir marka müşterilerine seslenirken hepsini aynı kabul etmek yerine alt segmentlerine ayırır. Daha odaklı bir iletişim.
# Kaynak sınırlı, yapılacak iş fazla olmasından kaynaklı bu çalışmalara yer verilir.

#Şirkete en fayda (kazanç, etkileşim, marka tanıtımı) sağlayan müşterilere daha fazla odaklanayım şeklinde bir segmentasyon yapılıp müşterilere odaklanılır.

#CRM Analitiği: Müşteriler ile iletişimi veriye dayalı yönetmek.
#Strateji geliştirme imkanı= Daha fazla müşteri +kazanç, daha az çaba ile daha fazla kaynak yaratma

#İş zekası uzmanlığı, veri analistliği, veri bilimi uzmanlığı=Veri analitiği çerçevesindeki pozisyonun önünü açabiliyor olacaktır.


#Temel Performans Göstergeleri (KPIs)
#Şirket, departman ya da çalışanların performanslarını değerlendirmek için kullanılan matematiksel göstergelerdir.

#Customer Acquisition Rate (Müşteri Kazanma Oranı): Belirli bir zamanda kazanılan müşteri yüzdesidir.
#Customer Retention Rate (Müşteri Elde Etme Oranı): 2. alışverişi yapan müşteri artık markaya biraz daha yakındır. 2. satın almasını yapan müşteri bir sonrakine kadar ne kadar zaman geçirdiyse elde etme oranı o şekilde hesaplanır.
#Customer Churn Rate (Müşteri Terk Oranı):
#Conversion Rate (Dönüşüm Oranı): Bir ilan sitesindeki ilanınız 1000 kişi gördü 10 kişi tıkladıysa bunun dönüşüm oranı 10/1000'dir.
#10 kişi tıkladı 1 kişi gelip satın aldıysa bunun dönüşüm oranı 1/10'dur.
#Reklamını gören-tıklayan-gelip alışveriş yapan
#Growth Rate (Büyüme Oranı):Şirketlerin orta uzun vadeli planları çerçevesinde, yılın en başında ya da belirli zaman periyotlarında koyduğu en genel çerçevedeki hedeflerdir.

#Kohort Analizi: Belirli bir KPI'ın belirli bir zamanda raporlanmasına denir.Ortak özelliklere sahip bir grup insanın davranışının analizidir.
#Cohort: Ortak özelliklere sahip 1 grup insan
#Churn Rate, retention rate (etc) 'leri hesaplanır.

#Uygulama indirme tarihleri ve retention rate değerleri

import pandas as pd
import datetime as dt
#('Invoice Date' = Fatura Tarihi)
df=pd.read_excel('HAFTA 3/online_retail_II.xlsx')
df['order_month']=df['InvoiceDate'].dt.to_period('M')
df.head()


#Yukarıdaki kod parçası perakende satış yapan bir firmanın verileri ile retention oranının kohort analizi için yapılan işlemlerden biridir. İşlemin amacı: Sipariş aylarını belirlemek
