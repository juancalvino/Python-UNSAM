saldo = 500_000.0
total_pagado = 0.0

tasa = 0.05

pago_mensual = 2684.11  
pago_extra = 1000  
pago_total = 0

mes_pagado = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108


while saldo > 0:
    if(mes_pagado >= pago_extra_mes_comienzo and mes_pagado <= pago_extra_mes_fin):
        pago_total = pago_mensual + pago_extra
    else:
        pago_total = pago_mensual   
    
    if(pago_total > saldo):
        pago_total = saldo 
        saldo -= pago_total
    else:
        saldo = saldo * (1+tasa/12) - pago_total

    mes_pagado += 1
    total_pagado += pago_total

    print(mes_pagado, total_pagado, saldo)

print('Total pagado: ', round(total_pagado, 2),
        '\nMeses: ', mes_pagado)
