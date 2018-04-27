#!/usr/bin/python
# -*- coding: utf-8 -*-
#Take only one word in lower case as argument
class TelexConverter():
	tone = u'sfxrj'
	consonant = u'qrtpsghklxcvbnm'
	tonemap = {u'f' : [u'ầ', u'à', u'ằ', u'è', u'ề', u'ò', u'ồ', u'ờ', u'ù', u'ừ', u'ì', u'ỳ']
	, u's': [u'ấ', u'á', u'ắ', u'é', u'ế', u'ó', u'ố', u'ớ', u'ú', u'ứ', u'í', u'ý']
	, u'r': [u'ẩ', u'ả', u'ẳ', u'ẻ', u'ể', u'ỏ', u'ổ', u'ở', u'ủ', u'ử', u'ỉ', u'ỷ']
	, u'x': [u'ẫ', u'ã', u'ẵ', u'ẽ', u'ễ', u'õ', u'ỗ', u'ỡ', u'ũ', u'ữ', u'ĩ', u'ỹ']
	, u'j': [u'ậ', u'ạ', u'ặ', u'ẹ', u'ệ', u'ọ', u'ộ', u'ợ', u'ụ', u'ự', u'ị', u'ỵ'] 
	, u'z': [u'â', u'a', u'ă', u'e', u'ê', u'o', u'ô', u'ơ', u'u', u'ư', u'i', u'y']}
	vietnameseCharMap = {u'aw': [u'ă', u'ắ', u'ằ', u'ặ', u'ẳ', u'ẵ'], u'aa': [u'â', u'ấ', u'ầ', u'ẩ', u'ẫ', u'ậ']
	, u'a': [u'a', u'á', u'à', u'ả', u'ã', u'ạ'],  u'oo': [u'ô', u'ố', u'ồ', u'ổ', u'ỗ', u'ộ']
	, u'ow': [u'ơ', u'ớ', u'ờ', u'ổ', u'ỗ', u'ộ'], u'o': [u'o', u'ó', u'ò', u'ỏ', u'õ', u'ọ']
	, u'ee': [u'ê', u'ế', u'ề', u'ể', u'ễ', u'ệ'], u'e': [u'e', u'é', u'è', u'ẻ', u'ẽ', u'ẹ']
	, u'uw': [u'ư', u'ứ', u'ừ', u'ử', u'ữ', u'ự'], u'u': [u'u', u'ú', u'ù', u'ủ', u'ũ', u'ụ']
	, u'i': [u'i', u'í', u'ì', u'ỉ', u'ĩ', u'ị'], u'dd': u'đ', u'y' : [u'ý', u'ỳ', u'ỹ', u'ỷ', u'ỵ', u'y'] }
	def ToRaw(self, word):
		newWord = u''
		tail = u''
		for char in word:
			if char in self.consonant:
				newWord = newWord + char
			else:
				for raw, tone in self.tonemap.items():
					if char in tone:
						tail = raw
				for raw, vnChar in self.vietnameseCharMap.items():
					if char in vnChar:
						newWord = newWord + raw
		if tail != u'z':
			newWord = newWord + tail
		return newWord
	def ToVietnamese(self, word):
		newWord = u''
		tail = word[-1]
		size = len(word) -1
		skip = 0
		if tail not in self.tone:
			tail = u'z'
			size = size + 1
		for i in range(0, size):
			end = True
			if i == size-1:
				end = False
			if skip > 0:
				skip -= 1
				continue
			print word[i]
			if word[i] in self.consonant:
				newWord = newWord + word[i]
			else:
				if word[i] == u'a':
					if word[i+1] == u'a':
						newWord = newWord + self.tonemap[tail][0]
						skip+=1
					elif word[i+1] == u'w':
						newWord = newWord + self.tonemap[tail][2]	
						skip+=1
					else:
						newWord = newWord + self.tonemap[tail][1]
					tail =u'z'
				elif word[i] == u'o':
					if end and word[i+1] == u'o':
						newWord = newWord + self.tonemap[tail][6]
						skip+=1
					elif end and word[i+1] == u'w':
						newWord = newWord + self.tonemap[tail][7]	
						skip+=1
					elif end and i+2<size and word[i+1:i+2] in [u'ac', u'aa']:
						 newWord = newWord + self.tonemap[u'z'][5]
						 continue
					else:
						newWord = newWord + self.tonemap[tail][5]
					tail = u'z'
				elif word[i] == u'e':
					if end and word[i+1] == u'e':
						newWord = newWord + self.tonemap[tail][4]
						skip+=1
					else:
						newWord = newWord + self.tonemap[tail][3]
					tail = u'z'
				elif word[i] == u'u':
					if ( i !=0 and word[i-1] == u'q') or (end and word[i+1] == u'y'):
						newWord = newWord + self.tonemap[u'z'][8]
					elif end and word[i+1] == u'w':
						if  i+2<size and word[i+2] == u'o':
							newWord = newWord + self.tonemap[u'z'][9]	
						else:
							newWord = newWord + self.tonemap[tail][9]
							tail = u'z'
						skip+=1
					elif (end and word[i+1] in u'oe') or (end and i+2<size and word[i+1:i+2] == u'aa') :
						newWord = newWord + self.tonemap[u'z'][8]	
					else:
						newWord = newWord + self.tonemap[tail][8]
						tail = u'z'
						skip+=1
				elif word[i] == u'i':	
					if (i!=0 and word[i-1] == u'g' and i != size-1) or (end and word[i+1] == u'e'):
						newWord = newWord + self.tonemap[u'z'][10]
					else:
						newWord = newWord + self.tonemap[tail][10]
						tail = u'z'
				elif word[i] == u'y':
					if end and word[i+1] == u'e':
						newWord = newWord + self.tonemap[u'z'][11]
					else:
						newWord = newWord + self.tonemap[tail][11]
						tail = u'z'
		return newWord