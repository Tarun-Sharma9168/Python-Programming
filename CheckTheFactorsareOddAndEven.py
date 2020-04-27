#That is only perfect squares are having the odd factors which are checked amazingly by taking modulo by 1
#Nice aPproach
def factor_group(num):
	return 'odd' if (num ** 0.5)%1 == 0 else 'even'
