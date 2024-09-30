import reflex as rx

def tyc() -> rx.Component:
    return rx.container(
        rx.text("Términos y Condiciones", class_name="font-bold text-2xl my-4"),
        rx.text("1. Introducción", class_name="font-bold my-2"),
        rx.text("Bienvenido a [Nombre de la Aplicación] ('Nosotros', 'Nuestro'). Al acceder o utilizar nuestra aplicación, aceptas cumplir y estar sujeto a los siguientes términos y condiciones ('Términos'). Si no aceptas estos términos, no debes usar nuestra aplicación."),
        
        rx.text("2. Uso de la Aplicación", class_name="font-bold my-2"),
        rx.text("Nuestra aplicación está destinada a [Descripción de la Función Principal de la Aplicación]. Los usuarios deben tener al menos 18 años para registrarse y utilizar los servicios proporcionados. Al acceder a la aplicación, aceptas utilizarla solo para los fines permitidos y de conformidad con estos Términos, así como con todas las leyes aplicables."),

        rx.text("3. Registro de Cuenta", class_name="font-bold my-2"),
        rx.text("Para utilizar ciertas funciones de nuestra aplicación, deberás crear una cuenta proporcionando información precisa y actualizada. Eres responsable de mantener la confidencialidad de tu cuenta y de cualquier actividad que ocurra bajo tu cuenta."),

        rx.text("4. Prohibiciones", class_name="font-bold my-2"),
        rx.text("No puedes:"),
        rx.unordered_list(
            rx.list_item("Usar la aplicación de manera ilegal o para fines no autorizados."),
            rx.list_item("Interferir con el funcionamiento de la aplicación o intentar vulnerar su seguridad."),
            rx.list_item("Recolectar datos de otros usuarios sin su consentimiento.")
        ),

        rx.text("5. Propiedad Intelectual", class_name="font-bold my-2"),
        rx.text("Todos los derechos de propiedad intelectual en la aplicación y su contenido (excepto el contenido proporcionado por los usuarios) son propiedad exclusiva de [Nombre de la Empresa o Aplicación]. No puedes reproducir, distribuir o modificar cualquier parte de la aplicación sin nuestra autorización previa."),

        rx.text("6. Limitación de Responsabilidad", class_name="font-bold my-2"),
        rx.text("Nos esforzamos por asegurar que nuestra aplicación funcione de manera correcta, pero no garantizamos su disponibilidad ininterrumpida ni la ausencia de errores. No seremos responsables de ninguna pérdida o daño indirecto que surja de tu uso de la aplicación."),

        rx.text("7. Modificaciones de los Términos", class_name="font-bold my-2"),
        rx.text("Nos reservamos el derecho de modificar estos Términos en cualquier momento. Si realizamos cambios sustanciales, te notificaremos mediante un aviso en la aplicación. El uso continuado de la aplicación después de la notificación de cambios constituye tu aceptación de los nuevos Términos."),

        rx.text("8. Contacto", class_name="font-bold my-2"),
        rx.text("Si tienes alguna pregunta sobre estos Términos, por favor contáctanos en [Correo Electrónico]."),

        class_name="bg-gray-200 text-black rounded"
    )