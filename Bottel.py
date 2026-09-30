
from telegram import Update

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

import calculadora as calc
import database


TOKEN = "8885901329:AAE6_QGqlhD9-FvdZ7hWRm09n6CFrz792qU"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    usuario = update.effective_user


    database.guardar_usuario(
        usuario.id,
        usuario.first_name,
        usuario.username
    )


    await update.message.reply_text(
        "¡Hola! 👋\n\n"
        "Elegí una opción:\n\n"
        "1️⃣ Calculadora\n"
        "2️⃣ Información del sistema\n"
        "3️⃣ Historial\n"
        "4️⃣ Salir"
    )


async def mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text



    if texto.strip() == "1":

        context.user_data["calculadora"] = True

        await update.message.reply_text(
            "🧮 Calculadora\n\n"
            "Escribí la operación de esta forma:\n\n"
            "10 + 5"
        )

        return




    elif texto == "2":

        await update.message.reply_text(
            "💻 Información del sistema\n\n"
            "Python Bot\n"
            "Base de datos: SQLite\n"
            "Calculadora: Python"
        )

        return




    elif texto == "3":

        telegram_id = update.effective_user.id

        historial = database.obtener_historial(telegram_id)

        if not historial:

            await update.message.reply_text(
                "📋 Todavía no tenés operaciones guardadas."
            )

            return

        mensaje_historial = "🧮 Tu historial:\n\n"

        for numero1, operador, numero2, resultado in historial:

            mensaje_historial += (
                f"{numero1:g} {operador} "
                f"{numero2:g} = {resultado}\n"
            )

        await update.message.reply_text(
            mensaje_historial
        )

        return




    elif texto == "4":

        context.user_data["calculadora"] = False

        await update.message.reply_text(
            "👋 ¡Hasta luego!"
        )

        return




    elif context.user_data.get("calculadora"):

        partes = texto.split()

        if len(partes) != 3:

            await update.message.reply_text(
                "❌ Formato incorrecto.\n\n"
                "Usá este formato:\n"
                "10 + 5"
            )

            return

        try:

            num1 = float(partes[0])
            operador = partes[1]
            num2 = float(partes[2])

            resultado = calc.calculadora(
                num1,
                num2,
                operador
            )

            
            database.guardar_operacion(
                update.effective_user.id,
                num1,
                operador,
                num2,
                resultado
            )

            await update.message.reply_text(
                f"✅ El resultado es: {resultado}"
            )

        except ValueError:

            await update.message.reply_text(
                "❌ Por favor, escribí números válidos."
            )

        return




    else:

        await update.message.reply_text(
            "❌ Opción no válida.\n\n"
            "Elegí una opción:\n\n"
            "1️⃣ Calculadora\n"
            "2️⃣ Información del sistema\n"
            "3️⃣ Historial\n"
            "4️⃣ Salir"
        )


database.crear_tablas()



app = Application.builder().token(TOKEN).build()



app.add_handler(
    CommandHandler("start", start)
)


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        mensaje
    )
)


print("Bot iniciado...")


app.run_polling()
