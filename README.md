<h1 align="left"> Scrapy </h1>

<b>Scrapy</b>, Python'da yazılmış, ücretsiz ve açık kaynaklı bir web tarama çerçevesidir. Orijinal olarak web kazıma için tasarlanmış olup, API'leri kullanarak veya genel amaçlı bir web tarayıcısı olarak veri çıkarmak için de kullanılabilir

Müşteriler, ürünleriniz ve hizmetleriniz hakkında sosyal medya, çevrimiçi forumlar ve hemen hemen tüm internet üzerinden istenmeyen geri bildirimler bırakıyor. Bu araç Sikayetvar sitesinden banka müşterilerinin hesap işlemleri,kredi kartları, atm işlemleri,kredi işlemleri gibi banka işlemleri hakkında sorunlarını dile getirdikleri verileri çekmek için yazılan bir bot aracıdır. Scrapy web sayfasını doğrudan kazıyamadığı için HTTP API'sine sahip hafif bir tarayıcı olarak <b>scrapy-splash</b> kullanılmıştır.

<h1 align="left"> Gereklilikler </h1>
<a href="https://www.python.org/downloads/" target="blank"><img align="center" src="https://img.shields.io/pypi/pyversions/Scrapy.svg"></a>

<a href="https://pypi.python.org/pypi/Scrapy" target="blank"><img align="center" src="https://img.shields.io/pypi/v/Scrapy.svg"></a>
```
pip install Scrapy
```
<a href="https://pypi.org/project/scrapy-splash/" target="blank"><img align="center" src="https://warehouse-camo.ingress.cmh1.psfhosted.org/2cbf025d98e1b5f88fe9cf799749232d23dbb19d/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7363726170792d73706c6173682e737667"></a>
```
pip install scrapy-splash
```
<h1 align="left"> Bot Uygulama Aşamaları </h1>

Terminal üzerinden projeyi başlatmak
```
scrapy startproject whiskyscraper
```
Proje üzerinde uygulamanın gerçekleşeceği dizine gitmek
```
cd whiskyscraper/whiskyscraper
```
Kabuğa geri dönmek
```
scrapy shell
```
Url'e request göndermek
```
fetch('https://www.sikayetvar.com/banka')
```
Html tag'lerine göre verileri çekmek için scrapy selector documentasyon: 

- https://docs.scrapy.org/en/latest/topics/selectors.html

Response ile seçilen bir div tag'indeki class'a ait python kodu: 
```
response.css(div.class)
```
Uygulamayı Çalıştırma ve Csv Dosyasına Kaydetme

```
scrapy crawl bankscraper -O bank.csv
```
