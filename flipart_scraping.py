import json,pprint,os,requests,time
from bs4 import BeautifulSoup
if os.path.exists("flipkart.json"):
	with open("flipkart.json","r") as g:
		k=json.load(g)
		h=k
else:
	h=[]
	for i in range(1,22):
		a=requests.get("https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_"+str(i))
		time.sleep(3)
		soup=BeautifulSoup(a.text,"lxml")
		b=soup.findAll("div",class_="_1UoZlX")
		for c in b:

			g={}
			g["Mobile"]=c.find("div", class_="_3wU53n").text
			e=c.findAll("li",class_="tVe95H")
			g["Price"]=c.find("div",class_="_1vC4OE _2rQ-NK").getText()
			g["Rating"]=c.find("div",class_="hGSR34").getText()
			n=c.find("a",class_="_31qSD5")
			n=requests.get("https://www.flipkart.com"+n["href"])
			n=BeautifulSoup(n.text,"lxml")
			n=n.find("ul",class_="LzhdeS")
			n=n.findAll("div",class_="_2_AcLJ")
			a=0
			img=""
			for ii in n[0]["style"]:
				if ii==")":
					a=0
				elif ii=="(":
					a=1
				elif a==1:
					img+=ii

			g["Image Link(url)"]=img
			for f in e:
				if "RAM" in f.text:
					a1=""
					for a2 in f.text:
						if a2!="|":
							a1+=a2
						else:
							a1+=","
					g["Memory"]=a1
				if "Display" in f.text:
					g["Display"]=f.text
				if "Camera" in f.text:
					a1=""
					for a2 in f.text:
						if a2!="|":
							a1+=a2
						else:
							a1+=","
					g["Camera"]=a1
				if "Battery" in f.text and "mAh" in f.text:
					g["Battery"]=f.text
				if "Processor" in f.text:
					g["Processor"]=f.text
				if "Warranty" in f.text:
					g["Warranty"]=f.text
			h.append(g)
	with open("flipkart.json","w+") as j:
		json.dump(h,j)
	print(len(h),"h")

pprint.pprint(h)


