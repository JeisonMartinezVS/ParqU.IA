import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from db import registrar_placa, obtener_tipo_y_rol
from detection import detectar_placa, calcular_precio, capturar_imagen_camara

def registrar():
    placa = entrada_placa.get().upper()
    tipo_vehiculo = tipo_var.get()
    rol = rol_var.get()
    
    if placa and tipo_vehiculo and rol:
        exito = registrar_placa(placa, tipo_vehiculo, rol)
        if exito:
            messagebox.showinfo("Registro", f"Placa {placa} registrada exitosamente.")
            limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", f"La placa {placa} ya está registrada.")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def cargar_imagen():
    ruta_imagen = filedialog.askopenfilename(
        title="Seleccionar imagen de la placa",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if ruta_imagen:
        placa = detectar_placa(ruta_imagen)
        if placa:
            resultado = obtener_tipo_y_rol(placa)
            if resultado:
                tipo_vehiculo, rol = resultado
                precio = calcular_precio(tipo_vehiculo, rol)
                if precio is not None:
                    messagebox.showinfo(
                        "Información de la Placa",
                        f"Placa: {placa}\nTipo de Vehículo: {tipo_vehiculo.capitalize()}\nRol: {rol.capitalize()}\nPrecio: ${precio:.2f}"
                    )
                else:
                    messagebox.showerror("Error", "No se pudo calcular el precio.")
            else:
                # Si la placa no está registrada, se asume como visitante
                precio = calcular_precio('carro', 'visitante')  # Asumimos 'carro' por defecto
                respuesta = messagebox.askyesno(
                    "Placa No Registrada",
                    f"La placa {placa} no está registrada.\nSe asume como Visitante.\nPrecio: ${precio:.2f}\n\n¿Desea registrar esta placa?"
                )
                if respuesta:
                    abrir_ventana_registro(placa)
        else:
            messagebox.showerror("Error", "No se pudo detectar la placa en la imagen seleccionada.")

def capturar_placa_camara():
    imagen_ruta = capturar_imagen_camara()
    if imagen_ruta:
        placa = detectar_placa(imagen_ruta)
        if placa:
            resultado = obtener_tipo_y_rol(placa)
            if resultado:
                tipo_vehiculo, rol = resultado
                precio = calcular_precio(tipo_vehiculo, rol)
                if precio is not None:
                    messagebox.showinfo(
                        "Información de la Placa",
                        f"Placa: {placa}\nTipo de Vehículo: {tipo_vehiculo.capitalize()}\nRol: {rol.capitalize()}\nPrecio: ${precio:.2f}"
                    )
                else:
                    messagebox.showerror("Error", "No se pudo calcular el precio.")
            else:
                # Si la placa no está registrada, se asume como visitante
                precio = calcular_precio('carro', 'visitante')  # Asumimos 'carro' por defecto
                respuesta = messagebox.askyesno(
                    "Placa No Registrada",
                    f"La placa {placa} no está registrada.\nSe asume como Visitante.\nPrecio: ${precio:.2f}\n\n¿Desea registrar esta placa?"
                )
                if respuesta:
                    abrir_ventana_registro(placa)
        else:
            messagebox.showerror("Error", "No se pudo detectar la placa en la imagen capturada.")

def abrir_ventana_registro(placa_detectada):
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrar Nueva Placa")
    ventana_registro.geometry("350x200")
    
    tk.Label(ventana_registro, text="Placa:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entrada_nueva_placa = tk.Entry(ventana_registro, width=20)
    entrada_nueva_placa.grid(row=0, column=1, padx=10, pady=10)
    entrada_nueva_placa.insert(0, placa_detectada)
    entrada_nueva_placa.config(state='disabled')
    
    tk.Label(ventana_registro, text="Tipo de Vehículo:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    tipo_nuevo_var = tk.StringVar(value="carro")
    opciones_tipo = ["carro", "moto"]
    menu_tipo = tk.OptionMenu(ventana_registro, tipo_nuevo_var, *opciones_tipo)
    menu_tipo.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    tk.Label(ventana_registro, text="Rol:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    rol_nuevo_var = tk.StringVar(value="visitante")
    opciones_rol = ["estudiante", "visitante"]
    menu_rol = tk.OptionMenu(ventana_registro, rol_nuevo_var, *opciones_rol)
    menu_rol.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    
    def registrar_nueva_placa():
        tipo_vehiculo = tipo_nuevo_var.get()
        rol = rol_nuevo_var.get()
        exito = registrar_placa(placa_detectada, tipo_vehiculo, rol)
        if exito:
            messagebox.showinfo("Registro", f"Placa {placa_detectada} registrada exitosamente.")
            ventana_registro.destroy()
        else:
            messagebox.showwarning("Advertencia", f"La placa {placa_detectada} ya está registrada.")
            ventana_registro.destroy()
    
    btn_registrar = tk.Button(ventana_registro, text="Registrar", command=registrar_nueva_placa)
    btn_registrar.grid(row=3, column=0, columnspan=2, pady=20)
    
def limpiar_campos():
    entrada_placa.delete(0, tk.END)
    tipo_var.set("carro")
    rol_var.set("visitante")

def iniciar_gui():
    
    ventana = tk.Tk()
    ventana.title("Sistema de Registro de Vehículos")
    ventana.geometry("400x400")
    
    # Frame para Registro Manual
    frame_registro = tk.LabelFrame(ventana, text="Registro Manual de Placas", padx=20, pady=20)
    frame_registro.pack(fill="both", expand="yes", padx=20, pady=10)
    
    tk.Label(frame_registro, text="Placa:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    global entrada_placa
    entrada_placa = tk.Entry(frame_registro, width=20)
    entrada_placa.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(frame_registro, text="Tipo de Vehículo:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global tipo_var
    tipo_var = tk.StringVar(value="Selecciona el tipo de vehiculo")
    opciones_tipo = ["carro", "moto"]
    menu_tipo = tk.OptionMenu(frame_registro, tipo_var, *opciones_tipo)
    menu_tipo.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    
    tk.Label(frame_registro, text="Rol:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    global rol_var
    rol_var = tk.StringVar(value="Tipo de Rol")
    opciones_rol = ["estudiante", "visitante"]
    menu_rol = tk.OptionMenu(frame_registro, rol_var, *opciones_rol)
    menu_rol.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    
    btn_registrar = tk.Button(frame_registro, text="Registrar Placa", width=15, command=registrar)
    btn_registrar.grid(row=3, column=0, columnspan=2, pady=10)
    
    # Frame para Detección de Placas
    frame_deteccion = tk.LabelFrame(ventana, text="Detección de Placas", padx=20, pady=20)
    frame_deteccion.pack(fill="both", expand="yes", padx=20, pady=10)
    
    btn_cargar_imagen = tk.Button(frame_deteccion, text="Cargar Imagen y Detectar Placa", width=25, command=cargar_imagen)
    btn_cargar_imagen.grid(row=0, column=0, pady=10)
    
    btn_captura_camara = tk.Button(frame_deteccion, text="Capturar Imagen desde Cámara", width=25, command=capturar_placa_camara)
    btn_captura_camara.grid(row=1, column=0, pady=10)
    
    ventana.mainloop()
