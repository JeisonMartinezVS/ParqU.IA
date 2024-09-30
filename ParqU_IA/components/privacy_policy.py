import reflex as rx

def privacy_policy() -> rx.Component:
    return rx.box(
        rx.text("Política de Privacidad", class_name="font-bold text-2xl my-4"),
        
        rx.text("1. Introducción", class_name="font-bold my-2"),
        rx.text("En [Nombre de la Aplicación] ('Nosotros', 'Nuestro'), respetamos tu privacidad y nos comprometemos a proteger la información personal que compartes con nosotros. Esta Política de Privacidad describe cómo recopilamos, utilizamos y protegemos tu información."),
        
        rx.text("2. Información que Recopilamos", class_name="font-bold my-2"),
        rx.text("Recopilamos la siguiente información cuando usas nuestra aplicación:"),
        rx.unordered_list(
            rx.list_item("Información personal, como tu nombre, correo electrónico y otros datos que proporcionas al registrarte."),
            rx.list_item("Datos de uso, como información sobre cómo interactúas con nuestra aplicación."),
            rx.list_item("Información técnica, como tu dirección IP y tipo de dispositivo.")
        ),
        
        rx.text("3. Uso de la Información", class_name="font-bold my-2"),
        rx.text("Utilizamos tu información para los siguientes fines:"),
        rx.unordered_list(
            rx.list_item("Proporcionar y mantener el funcionamiento de nuestra aplicación."),
            rx.list_item("Personalizar tu experiencia y ofrecer contenido relevante."),
            rx.list_item("Comunicarnos contigo sobre actualizaciones, notificaciones y soporte."),
            rx.list_item("Mejorar la seguridad y prevenir fraudes o actividades ilegales.")
        ),

        rx.text("4. Compartición de la Información", class_name="font-bold my-2"),
        rx.text("No compartimos tu información personal con terceros, excepto en las siguientes circunstancias:"),
        rx.unordered_list(
            rx.list_item("Con proveedores de servicios que nos ayudan a operar la aplicación y solo tienen acceso a la información necesaria para realizar sus funciones."),
            rx.list_item("Cuando sea requerido por ley o en respuesta a solicitudes legales válidas de autoridades gubernamentales."),
            rx.list_item("En caso de fusión, adquisición o venta de activos, tu información puede ser transferida como parte del acuerdo.")
        ),

        rx.text("5. Seguridad de la Información", class_name="font-bold my-2"),
        rx.text("Tomamos medidas de seguridad razonables para proteger tu información personal. Sin embargo, no podemos garantizar la seguridad completa de los datos transmitidos a través de Internet o almacenados en nuestros sistemas."),
        
        rx.text("6. Retención de la Información", class_name="font-bold my-2"),
        rx.text("Retenemos tu información personal solo durante el tiempo necesario para cumplir con los fines descritos en esta política o según lo requerido por la ley."),
        
        rx.text("7. Derechos del Usuario", class_name="font-bold my-2"),
        rx.text("Tienes derecho a acceder, corregir o eliminar tu información personal que almacenamos. Para ejercer estos derechos, contáctanos en [Correo Electrónico]."),
        
        rx.text("8. Cambios en la Política de Privacidad", class_name="font-bold my-2"),
        rx.text("Podemos actualizar esta Política de Privacidad en cualquier momento. Si realizamos cambios importantes, te notificaremos mediante un aviso en la aplicación."),
        
        rx.text("9. Contacto", class_name="font-bold my-2"),
        rx.text("Si tienes preguntas sobre esta Política de Privacidad, contáctanos en [Correo Electrónico]."),
        
        class_name="p-4 bg-gray-200 text-black rounded"
    )
