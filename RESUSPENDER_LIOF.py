from ctypes import c_void_p


conc_liof_ug = 5
vol_resusp = 20
conc_resusp_ug = conc_liof_ug/vol_resusp
conc_resusp_ng = conc_resusp_ug*1000
print(f'{"Tienes: "}{vol_resusp}{"uL"}{" "}{"a una concentracion de"}{" "}{conc_resusp_ng}{"ng/uL"}')