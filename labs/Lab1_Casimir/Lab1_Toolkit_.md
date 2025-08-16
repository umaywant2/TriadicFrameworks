{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Casimir Resonance Visualization\n",
    "## Mythic Preface\n",
    "_\"Two plates whisper across the void, and the vacuum sings back.\"_\n",
    "\n",
    "This notebook simulates the Casimir effect using triadic field overlays. We explore how vacuum pressure emerges from nested dimensional resonance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports and Setup\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from ipywidgets import interact, FloatSlider"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Casimir Force Function (Triadic Interpretation)\n",
    "def casimir_force(d, A=1.0, hbar=1.0545718e-34, c=3e8):\n",
    "    classical = - (np.pi**2 * hbar * c) / (240 * d**4)\n",
    "    triadic = classical * np.sin(np.pi / d)\n",
    "    return classical, triadic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Interactive Plot\n",
    "def plot_force(d):\n",
    "    classical, triadic = casimir_force(d)\n",
    "    plt.figure(figsize=(8,5))\n",
    "    plt.bar(['Classical', 'Triadic'], [classical, triadic], color=['gray', 'purple'])\n",
    "    plt.title(f'Casimir Force at d = {d:.2e} m')\n",
    "    plt.ylabel('Force (N)')\n",
    "    plt.grid(True)\n",
    "    plt.show()\n",
    "\n",
    "interact(plot_force, d=FloatSlider(min=1e-9, max=1e-7, step=1e-9, value=5e-9))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Field Visualization\n",
    "x = np.linspace(-1, 1, 400)\n",
    "y = np.linspace(-1, 1, 400)\n",
    "X, Y = np.meshgrid(x, y)\n",
    "Z = np.sin(np.pi * X) * np.sin(np.pi * Y)\n",
    "\n",
    "plt.figure(figsize=(6,6))\n",
    "plt.contourf(X, Y, Z, cmap='plasma')\n",
    "plt.title('Triadic Field Between Plates')\n",
    "plt.axis('equal')\n",
    "plt.colorbar(label='Field Intensity')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mythic Reflection\n",
    "The Casimir force is not just a quantum artifact—it’s a whisper from the void, shaped by the geometry of resonance. In triadic terms, the vacuum is alive with phase, and the plates become instruments in a cosmic orchestra."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
