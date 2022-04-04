class Boleta:
    def __init__(self,categoria,horas_extras,minutos_tardanza):
        self.categoria=categoria
        self.horas_extras=horas_extras
        self.minutos_tardanza=minutos_tardanza

    def Categoria(self):
        print("CATEGORIA:            ",self.categoria)
    
    def Horas_extras(self):
        print("HORAS EXTRAS:         ",self.horas_extras)
    
    def tardanza(self):
        print("TARDANZAS: (minutos)  ",self.minutos_tardanza) 
    
                   
    def sueldo(self):
        if self.categoria.lower() =="a":
            sueldo_basico=3000
            print("SUELDO BASICO:        ",sueldo_basico)   
        
        elif self.categoria.lower() =="b":
            sueldo_basico=2500    
            print("SUELDO BASICO:        ",sueldo_basico)  
            
        elif self.categoria.lower() =="c":
            sueldo_basico=2000 
            print("SUELDO BASICO:        ",sueldo_basico)   
        else:
            print("Categoría no válida")
            
    def descuento(self):
        if self.categoria.lower() =="a":
            sueldo_basico=3000

        elif self.categoria.lower() =="b":
            sueldo_basico=2500    
       
        elif self.categoria.lower() =="c":
            sueldo_basico=2000 
            
        descuento_tardanza=((sueldo_basico/240)/60)*self.minutos_tardanza
        print("DESCUENTO TARDANZA:   ",round(descuento_tardanza,2))
        
    def extra(self):
        if self.categoria.lower() =="a":
            sueldo_basico=3000
   
        elif self.categoria.lower() =="b":
            sueldo_basico=2500    
 
        elif self.categoria.lower() =="c":
            sueldo_basico=2000 
            
        pago_horas_extras= (sueldo_basico/240)*self.horas_extras   
        print("PAGO POR HORAS EXTRAS:",round(pago_horas_extras,2))
    
    def total(self):
        if self.categoria.lower() =="a":
            sueldo_basico=3000
   
        elif self.categoria.lower() =="b":
            sueldo_basico=2500    
 
        elif self.categoria.lower() =="c":
            sueldo_basico=2000 
            
        descuento_tardanza=((sueldo_basico/240)/60)*self.minutos_tardanza    
        pago_horas_extras= (sueldo_basico/240)*self.horas_extras 
        sueldo_neto=sueldo_basico-descuento_tardanza+pago_horas_extras
        print("SUELDO NETO:          ",round(sueldo_neto,2))
        