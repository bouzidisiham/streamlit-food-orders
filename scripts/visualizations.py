import matplotlib.pyplot as plt

def plot_payment_methods(data):
    """
    Diagramme circulaire des méthodes de paiement.
    """
    fig, ax = plt.subplots()
    data['Payment Method'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_ylabel("")
    ax.set_title("Répartition des Méthodes de Paiement")
    return fig

def plot_orders_by_restaurant(data):
    """
    Barres horizontales : Nombre de commandes par restaurant.
    """
    fig, ax = plt.subplots()
    data['Restaurant ID'].value_counts().head(10).plot(kind='bar', ax=ax, color='orange')
    ax.set_title("Top 10 Restaurants par Nombre de Commandes")
    ax.set_xlabel("Restaurant ID")
    ax.set_ylabel("Nombre de Commandes")
    return fig

def plot_orders_over_time(data):
    """
    Courbe d'évolution des commandes dans le temps.
    """
    fig, ax = plt.subplots()
    data.set_index('Order Date and Time').resample('D')['Order ID'].count().plot(ax=ax)
    ax.set_title("Nombre de Commandes par Jour")
    ax.set_ylabel("Nombre de Commandes")
    return fig

def plot_order_value_distribution(data):
    """
    Histogramme de la distribution des valeurs des commandes.
    """
    fig, ax = plt.subplots()
    data['Order Value'].plot(kind='hist', bins=20, color='green', edgecolor='black', ax=ax)
    ax.set_title("Distribution des Valeurs des Commandes")
    ax.set_xlabel("Valeur de Commande (€)")
    return fig

def plot_delivery_fee_vs_order_value(data):
    """
    Nuage de points : Frais de livraison vs Valeur des commandes.
    """
    fig, ax = plt.subplots()
    ax.scatter(data['Order Value'], data['Delivery Fee'], alpha=0.5, color='purple')
    ax.set_title("Relation entre Valeur des Commandes et Frais de Livraison")
    ax.set_xlabel("Valeur de Commande (€)")
    ax.set_ylabel("Frais de Livraison (€)")
    return fig
