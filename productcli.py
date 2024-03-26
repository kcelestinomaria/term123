import typer
from rich.console import Console
from rich.table import Table
from model import Product
from database import get_all_products, delete_product, insert_product, complete_product, update_product


console = Console()

app = typer.Typer()


@app.command(short_help='adds a product')
def add(product: str, category: str):
    typer.echo(f"adding {product}, {category}")

    product = Product(product, category)
    insert_product(product)
    show()

@app.command(short_help='deletes a product')
def delete(position: int):
    typer.echo(f"deleting {position}")
    # indices in UI begin at 1, but in database at 0
    delete_product(position-1)
    show()

@app.command(short_help='updates a product')
def update(position: int, product: str = "", category: str = ""):
    typer.echo(f"updating {position}")
    update_product(position-1, product, category)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_product(position-1)
    show()

@app.command()
def show():
    products = get_all_products()
    console.print("[bold magenta]Products[/bold magenta]!", "")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Product", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Purchased", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Smartphones': 'cyan', 'Laptops': 'red', 'Smartwatches': 'cyan', 'Tablets': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, product in enumerate(products, start=1):
        c = get_category_color(product.category)
        is_purchased_str = ':true' if product.status == 2 else ':false'
        table.add_row(str(idx), product.product, f'[{c}]{product.category}[/{c}]', is_purchased_str)

    console.print(table)

if __name__ == "__main__":
    app()