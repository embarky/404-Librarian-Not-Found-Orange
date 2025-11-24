# src/config.py
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "../kaggle_data"
MODEL_PATH = "../models"
SUBMISSION_PATH = "../submission_data"
MODEL_PATH = "../models"
TOP_K = 10
SEED = 42


def set_plot_style(brand_blue: str = "#005C9E", dpi: int = 200):

    # Seaborn color palette: only main color
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    sns.set_palette([brand_blue])

    # Improve figure quality
    plt.rcParams['figure.dpi'] = dpi
    plt.rcParams['savefig.dpi'] = 300  # high-resolution when saving