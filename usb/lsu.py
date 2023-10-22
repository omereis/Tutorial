import usb.core
import usb.backend.libusb1

dev = usb.core.find(find_all=True)

for d in dev:
    #print (usb.util.get_string(d,128,d.iManufacturer))
    #print (usb.util.get_string(d,128,d.iProduct))
    print('++++++++++++++++++++++++++++++++++++++')
    print (f'Product ID={d.idProduct}')
    print (f'Vendor ID={d.idVendor}')
    print (f'Address={d.address}')
    print (f'Product={d.product}')


#busses = usb.busses()
#for bus in busses:
    #devices = bus.devices
    #for dev in devices:
        #if dev != None:
            #print(dir(dev))
            #print (f'iManufacturer ID={dev.iManufacturer}')
            #print (f'configurations={dev.configurations}')
            #try:
                #xdev = usb.core.find(idVendor=dev.idVendor, idProduct=dev.idProduct)
                #if xdev._manufacturer is None:
                    #xdev._manufacturer = usb.util.get_string(xdev, xdev.iManufacturer)
                #if xdev._product is None:
                    #xdev._product = usb.util.get_string(xdev, xdev.iProduct)
                #stx = '%6d %6d: '+str(xdev._manufacturer).strip()+' = '+str(xdev._product).strip()
                #print (f"stx {dev.idVendor},{dev.idProduct}")
                #print(dir(dev))
            #except:
                #pass
