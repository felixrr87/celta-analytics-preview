{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Preview de análisis de datos - Real Club Celta de Vigo\n",
    "Este notebook contiene un ejemplo listo para subir al repositorio, usando datos ficticios para demostrar la estructura de análisis y visualizaciones sin exponer información real."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import matplotlib.patheffects as path_effects\n",
    "\n",
    "# Configuración de estilo profesional\n",
    "plt.style.use('seaborn-v0_8')\n",
    "sns.set_palette('husl')\n",
    "\n",
    "# Datos de ejemplo ficticios\n",
    "datos = {\n",
    "    'Player': ['Jugador1', 'Jugador2', 'Jugador3', 'Jugador4'],\n",
    "    'Pos': ['MF', 'FW', 'DF', 'MF'],\n",
    "    'Age': ['21', '28', '24', '22'],\n",
    "    '90s': [900, 1800, 1350, 720],\n",
    "    'Gls': [5, 8, 0, 2],\n",
    "    'SoT': [20, 35, 5, 10],\n",
    "    'Sh': [50, 60, 10, 15],\n",
    "    'xG': [4.5, 7.0, 0.5, 1.8],\n",
    "    'SCA90': [1.2, 0.5, 0.3, 2.0],\n",
    "    'GCA90': [0.4, 0.2, 0.1, 0.5],\n",
    "    'Tkl+Int': [10, 2, 15, 8],\n",
    "    'PrgP': [5, 3, 1, 4]\n",
    "}\n",
    "\n",
    "df_preview = pd.DataFrame(datos)\n",
    "df_preview['Minutos'] = df_preview['90s']\n",
    "df_preview['Edad_num'] = df_preview['Age'].astype(int)\n",
    "\n",
    "df_preview"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Ejemplo de gráfico comparativo de jóvenes vs veteranos\n",
    "jovenes = df_preview[df_preview['Edad_num'] < 24]\n",
    "veteranos = df_preview[df_preview['Edad_num'] >= 24]\n",
    "\n",
    "categorias = ['Jóvenes (<24)', 'Veteranos (24+)']\n",
    "sca_values = [jovenes['SCA90'].mean(), veteranos['SCA90'].mean()]\n",
    "gca_values = [jovenes['GCA90'].mean(), veteranos['GCA90'].mean()]\n",
    "\n",
    "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))\n",
    "ax1.bar(categorias, sca_values, color=['#67B7D1','#003366'])\n",
    "ax1.set_title('SCA90: Jóvenes vs Veteranos')\n",
    "ax1.set_ylabel('SCA90')\n",
    "\n",
    "ax2.bar(categorias, gca_values, color=['#67B7D1','#003366'])\n",
    "ax2.set_title('GCA90: Jóvenes vs Veteranos')\n",
    "ax2.set_ylabel('GCA90')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}},
 "nbformat": 4,
 "nbformat_minor": 5
}
