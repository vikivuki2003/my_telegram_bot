from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Food', 'Drinks']

description_for_info_pages = {
    "main": "Welcome!",
    "about": "Cafe Victoria.\nThe operating hours are 24/7.",
    "payment": as_marked_section(
        Bold("Payment options:"),
        "By card in bot",
        "By card/cash after receiving",
        "In cafe",
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Delivery options:"),
            "Courier",
            "Takeaway",
            "Dine in",
            marker="✅ ",
        ),
        as_marked_section(Bold("Forbidden:"), "Mail", "Gull", marker="❌ "),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Categories:',
    'cart': 'The cart is empty!'
}