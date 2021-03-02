from mymodule import myping,get_ips_from_xl

for ip in get_ips_from_xl("ips.xls"):
	myping(ip)
