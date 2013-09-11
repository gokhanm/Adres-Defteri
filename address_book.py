#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sqlite3

class Database(object):
	def __init__(self, filename="address_book.db"):
		self.dbfilename = filename
		db = sqlite3.connect(self.dbfilename)
		c = db.cursor()
		c.execute(
			"CREATE TABLE IF NOT EXISTS records\
			(record_id INTEGER PRIMARY KEY, \
			name TEXT, \
			phone_number TEXT, \
			email_address TEXT \
			)" \
			)
		db.commit()
		c.close()

	def add_record(self, name='', phone_number='', email_address=''):
		db = sqlite3.connect(self.dbfilename)
		c = db.cursor()
		c.execute ("INSERT INTO records(name, phone_number, email_address) \
			VALUES (?,?,?)", (name, phone_number, email_address))
		db.commit()
		c.close()

	def delete_record(self, record_id):
		db = sqlite3.connect(self.dbfilename)
		c = db.cursor()
		c.execute('DELETE FROM records WHERE record_id = ?', (record_id,))
		db.commit()
		c.close()

	def list_all(self, ):
		db = sqlite3.connect(self.dbfilename)
		c = db.cursor()
		c.execute(''.join(['SELECT * FROM records']))
		records = c.fetchall()
		c.close()
		return records

#	def get_record(self, record):
#		db = sqlite3.connect(self.dbfilename)
#		c = db.cursor()
#		c.execute('SELECT * FROM records WHERE record_id = ?', (record,))
#		records = c.fetchall()
#		c.close()
#		return records


db_ = Database()

while True:

	try:

		print """
		Yapılacak Işlemi Seçiniz...
		-----------------
		1) Adresleri Listele
		2) Adres Ekle
		3) Adres Sil
		4) Çıkış
		"""

		girdi = input("Lütfen bir işlem seçiniz: ")
	

		if girdi == 1:
			liste = db_.list_all()
			FORMAT = '%-8s%-18s%-18s%-20s'
			print FORMAT % ('Sıra', 'Isim Soyisim', 'Telefon', 'Email Adresi')
			print '-' * 50
			for row in liste:
				print FORMAT % row

		elif girdi == 2:
			name = raw_input("Isim Soyisim: ")
			phone_number = raw_input("Telefon Numarasi: ")
			email_address = raw_input("Email Adresi: ")
			db_.add_record(name, phone_number, email_address)
			print "\nKayıt Eklenmiştir."
	
		elif girdi == 3:
			girdi = input("Silinecek kaydın sıra numarasını giriniz: ")
			db_.delete_record(girdi)
			print "\nKayıt silinmiştir."
	
#		elif girdi == 4:
#			girdi = raw_input("Lütfen id numarasını giriniz: ")
#			otp = db_.get_record(girdi)
#			FORMAT = '%-8s%-18s%-18s%-20s'
#			print FORMAT % ('Sıra', 'Isim Soyisim', 'Telefon', 'Email Adresi')
#			print '-' * 50
#			for row in otp:
#				print FORMAT % row
		else:
			quit()
	except (SyntaxError, KeyboardInterrupt):		#Herhangi bir işlem seçmeden Ctrl+enter yada enter tuşuna basılırsa
		print "\n UYARI !! Lütfen bir işlem seçiniz. Programı kapamak için çıkış yapınız"
