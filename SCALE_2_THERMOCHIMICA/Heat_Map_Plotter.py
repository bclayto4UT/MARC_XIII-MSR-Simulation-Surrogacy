import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
import json

# Periodic table data to replace bokeh dependency
def get_periodic_table_data():
    # Format: symbol, name, atomic number, group, period
    elements_data = [
        ('H', 'Hydrogen', 1, 1, 1),
        ('He', 'Helium', 2, 18, 1),
        ('Li', 'Lithium', 3, 1, 2),
        ('Be', 'Beryllium', 4, 2, 2),
        ('B', 'Boron', 5, 13, 2),
        ('C', 'Carbon', 6, 14, 2),
        ('N', 'Nitrogen', 7, 15, 2),
        ('O', 'Oxygen', 8, 16, 2),
        ('F', 'Fluorine', 9, 17, 2),
        ('Ne', 'Neon', 10, 18, 2),
        ('Na', 'Sodium', 11, 1, 3),
        ('Mg', 'Magnesium', 12, 2, 3),
        ('Al', 'Aluminum', 13, 13, 3),
        ('Si', 'Silicon', 14, 14, 3),
        ('P', 'Phosphorus', 15, 15, 3),
        ('S', 'Sulfur', 16, 16, 3),
        ('Cl', 'Chlorine', 17, 17, 3),
        ('Ar', 'Argon', 18, 18, 3),
        ('K', 'Potassium', 19, 1, 4),
        ('Ca', 'Calcium', 20, 2, 4),
        ('Sc', 'Scandium', 21, 3, 4),
        ('Ti', 'Titanium', 22, 4, 4),
        ('V', 'Vanadium', 23, 5, 4),
        ('Cr', 'Chromium', 24, 6, 4),
        ('Mn', 'Manganese', 25, 7, 4),
        ('Fe', 'Iron', 26, 8, 4),
        ('Co', 'Cobalt', 27, 9, 4),
        ('Ni', 'Nickel', 28, 10, 4),
        ('Cu', 'Copper', 29, 11, 4),
        ('Zn', 'Zinc', 30, 12, 4),
        ('Ga', 'Gallium', 31, 13, 4),
        ('Ge', 'Germanium', 32, 14, 4),
        ('As', 'Arsenic', 33, 15, 4),
        ('Se', 'Selenium', 34, 16, 4),
        ('Br', 'Bromine', 35, 17, 4),
        ('Kr', 'Krypton', 36, 18, 4),
        ('Rb', 'Rubidium', 37, 1, 5),
        ('Sr', 'Strontium', 38, 2, 5),
        ('Y', 'Yttrium', 39, 3, 5),
        ('Zr', 'Zirconium', 40, 4, 5),
        ('Nb', 'Niobium', 41, 5, 5),
        ('Mo', 'Molybdenum', 42, 6, 5),
        ('Tc', 'Technetium', 43, 7, 5),
        ('Ru', 'Ruthenium', 44, 8, 5),
        ('Rh', 'Rhodium', 45, 9, 5),
        ('Pd', 'Palladium', 46, 10, 5),
        ('Ag', 'Silver', 47, 11, 5),
        ('Cd', 'Cadmium', 48, 12, 5),
        ('In', 'Indium', 49, 13, 5),
        ('Sn', 'Tin', 50, 14, 5),
        ('Sb', 'Antimony', 51, 15, 5),
        ('Te', 'Tellurium', 52, 16, 5),
        ('I', 'Iodine', 53, 17, 5),
        ('Xe', 'Xenon', 54, 18, 5),
        ('Cs', 'Cesium', 55, 1, 6),
        ('Ba', 'Barium', 56, 2, 6),
        ('La', 'Lanthanum', 57, 3, 6),
        ('Ce', 'Cerium', 58, 0, 0),  # Lanthanide
        ('Pr', 'Praseodymium', 59, 0, 0),  # Lanthanide
        ('Nd', 'Neodymium', 60, 0, 0),  # Lanthanide
        ('Pm', 'Promethium', 61, 0, 0),  # Lanthanide
        ('Sm', 'Samarium', 62, 0, 0),  # Lanthanide
        ('Eu', 'Europium', 63, 0, 0),  # Lanthanide
        ('Gd', 'Gadolinium', 64, 0, 0),  # Lanthanide
        ('Tb', 'Terbium', 65, 0, 0),  # Lanthanide
        ('Dy', 'Dysprosium', 66, 0, 0),  # Lanthanide
        ('Ho', 'Holmium', 67, 0, 0),  # Lanthanide
        ('Er', 'Erbium', 68, 0, 0),  # Lanthanide
        ('Tm', 'Thulium', 69, 0, 0),  # Lanthanide
        ('Yb', 'Ytterbium', 70, 0, 0),  # Lanthanide
        ('Lu', 'Lutetium', 71, 0, 0),  # Lanthanide
        ('Hf', 'Hafnium', 72, 4, 6),
        ('Ta', 'Tantalum', 73, 5, 6),
        ('W', 'Tungsten', 74, 6, 6),
        ('Re', 'Rhenium', 75, 7, 6),
        ('Os', 'Osmium', 76, 8, 6),
        ('Ir', 'Iridium', 77, 9, 6),
        ('Pt', 'Platinum', 78, 10, 6),
        ('Au', 'Gold', 79, 11, 6),
        ('Hg', 'Mercury', 80, 12, 6),
        ('Tl', 'Thallium', 81, 13, 6),
        ('Pb', 'Lead', 82, 14, 6),
        ('Bi', 'Bismuth', 83, 15, 6),
        ('Po', 'Polonium', 84, 16, 6),
        ('At', 'Astatine', 85, 17, 6),
        ('Rn', 'Radon', 86, 18, 6),
        ('Fr', 'Francium', 87, 1, 7),
        ('Ra', 'Radium', 88, 2, 7),
        ('Ac', 'Actinium', 89, 3, 7),
        ('Th', 'Thorium', 90, 0, 0),  # Actinide
        ('Pa', 'Protactinium', 91, 0, 0),  # Actinide
        ('U', 'Uranium', 92, 0, 0),  # Actinide
        ('Np', 'Neptunium', 93, 0, 0),  # Actinide
        ('Pu', 'Plutonium', 94, 0, 0),  # Actinide
        ('Am', 'Americium', 95, 0, 0),  # Actinide
        ('Cm', 'Curium', 96, 0, 0),  # Actinide
        ('Bk', 'Berkelium', 97, 0, 0),  # Actinide
        ('Cf', 'Californium', 98, 0, 0),  # Actinide
        ('Es', 'Einsteinium', 99, 0, 0),  # Actinide
        ('Fm', 'Fermium', 100, 0, 0),  # Actinide
        ('Md', 'Mendelevium', 101, 0, 0),  # Actinide
        ('No', 'Nobelium', 102, 0, 0),  # Actinide
        ('Lr', 'Lawrencium', 103, 0, 0),  # Actinide
        ('Rf', 'Rutherfordium', 104, 4, 7),
        ('Db', 'Dubnium', 105, 5, 7),
        ('Sg', 'Seaborgium', 106, 6, 7),
        ('Bh', 'Bohrium', 107, 7, 7),
        ('Hs', 'Hassium', 108, 8, 7),
        ('Mt', 'Meitnerium', 109, 9, 7),
        ('Ds', 'Darmstadtium', 110, 10, 7),
        ('Rg', 'Roentgenium', 111, 11, 7),
        ('Cn', 'Copernicium', 112, 12, 7),
        ('Nh', 'Nihonium', 113, 13, 7),
        ('Fl', 'Flerovium', 114, 14, 7),
        ('Mc', 'Moscovium', 115, 15, 7),
        ('Lv', 'Livermorium', 116, 16, 7),
        ('Ts', 'Tennessine', 117, 17, 7),
        ('Og', 'Oganesson', 118, 18, 7)
    ]
    
    # Create DataFrame
    df = pd.DataFrame(elements_data, columns=['symbol', 'name', 'atomic number', 'group', 'period'])
    return df

def plot_abundance_matplotlib(
    json_file: str,
    time_step: int = 0,
    output_filename: str = 'Mole_percent_periodic_table.png',
    cmap: str = 'viridis',
    log_scale: bool = True,
    figsize: tuple = (16, 10),
    dpi: int = 600  # Increased DPI for poster presentation
):
    # Get our own periodic table data instead of using bokeh
    elements_copy = get_periodic_table_data()
    
    # Read the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract data for the requested time step
    if str(time_step) not in data["surrogate_vector"]:
        available_steps = list(data["surrogate_vector"].keys())
        raise ValueError(f"Time step {time_step} not found. Available time steps: {available_steps}")
    
    time_data = data["surrogate_vector"][str(time_step)]
    
    # Prepare data
    data_elements = []
    data_list = []
    for element, values in time_data.items():
        if "mole_percent" in values:
            try:
                mole_percent = float(values["mole_percent"])
                if mole_percent > 0:  # Only include positive values for log scale
                    data_elements.append(element)
                    data_list.append(mole_percent)
            except (ValueError, TypeError):
                print(f"Warning: Could not convert mole_percent value for {element}")

    if not data_list:
        raise ValueError(f"No valid mole_percent data found for time step {time_step}")
    
    # Create the figure and axis with white background
    fig, ax = plt.subplots(figsize=figsize, facecolor='white')
    ax.set_facecolor('white')
    
    # Create a grid to store colors - use white as background color
    color_grid = np.full((10, 20, 4), mcolors.to_rgba('white'), dtype=float)
    
    # Choose colormap
    cmap_funcs = {
        'plasma': cm.plasma,
        'inferno': cm.inferno,
        'magma': cm.magma,
        'viridis': cm.viridis,
        'cividis': cm.cividis,
        'turbo': cm.turbo
    }
    
    # Validate and select colormap
    cmap = cmap.lower()
    if cmap not in cmap_funcs:
        raise ValueError(f"Invalid color map: '{cmap}'. Valid options are: {', '.join(cmap_funcs.keys())}")
    
    # Get the colormap and invert it
    cmap_func = cmap_funcs[cmap]
    cmap_func_r = cmap_funcs[cmap].reversed()  # Invert the colormap
    
    # Prepare color scaling
    data = np.array(data_list)
    if log_scale:
        # Filter out non-positive values for log scale
        valid_mask = data > 0
        data = data[valid_mask]
        data_elements = [data_elements[i] for i in range(len(data_elements)) if valid_mask[i]]
        
        # Use a reasonable minimum value for log scale to avoid issues with very small numbers
        vmin = max(data.min(), 1e-10)
        norm = LogNorm(vmin=vmin, vmax=data.max())
    else:
        norm = Normalize(vmin=data.min(), vmax=data.max())
    
    # Color mapping using the inverted colormap
    color_scale = cmap_func_r(norm(data))
    
    # Define lanthanides and actinides
    lanthanides = [
        'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 
        'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'
    ]
    
    actinides = [
        'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 
        'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'
    ]
    
    # Map elements to their positions
    for _, row in elements_copy.iterrows():
        symbol = row['symbol']
        
        group = row['group']
        period = row['period']
        
        # Correctly position Lanthanides and Actinides
        if symbol in lanthanides:
            period = 8
            group = lanthanides.index(symbol) + 3  # Start at column 3
        elif symbol in actinides:
            period = 9
            group = actinides.index(symbol) + 3  # Start at column 3
        
        # Find the matching element in the abundance data (case insensitive)
        if group > 0 and period > 0:
            matching_idx = [i for i, s in enumerate(data_elements) if s.lower() == symbol.lower()]

            if matching_idx:
                # Use the first matching element (in case of duplicates)
                color_grid[period-1, group-1] = color_scale[matching_idx[0]]

    # Plot the periodic table
    im = ax.imshow(color_grid)

    # Annotate elements
    for _, row in elements_copy.iterrows():
        symbol = row['symbol']
        
        group = row['group']
        period = row['period']
        
        # Correctly position Lanthanides and Actinides
        if symbol in lanthanides:
            period = 8
            group = lanthanides.index(symbol) + 3  # Start at column 3
        elif symbol in actinides:
            period = 9
            group = actinides.index(symbol) + 3  # Start at column 3
        
        if group > 0 and period > 0:
            # Adjust indices for zero-based indexing
            group_idx = group - 1
            period_idx = period - 1
            
            # Add rectangle box behind each element
            rect = Rectangle((group_idx-0.5, period_idx-0.5), 1, 1, 
                            fill=False, 
                            edgecolor='gray', 
                            linewidth=1)
            ax.add_patch(rect)

            # Determine text color based on background
            bg_color = color_grid[period_idx, group_idx]
            text_color = 'black' if np.mean(bg_color[:3]) > 0.5 else 'white'
            
            # Add element symbol
            ax.text(group_idx, period_idx, symbol, ha='center', va='center', 
                    fontweight='bold', fontsize=12, color=text_color)
            
            # Add atomic number
            ax.text(group_idx, period_idx+0.3, str(row['atomic number']), ha='center', va='center', 
                    fontsize=8, color=text_color)
            
            # Add mole percent for elements in our data
            if symbol.lower() in [s.lower() for s in data_elements]:
                idx = [i for i, s in enumerate(data_elements) if s.lower() == symbol.lower()][0]
                value = data_list[idx]
                if value >= 0.01:
                    # Only show value if it's significant enough
                    formatted_value = f"{value:.2f}%" if value < 10 else f"{value:.1f}%"
                    ax.text(group_idx, period_idx-0.3, formatted_value, ha='center', va='center',
                            fontweight='bold', fontsize=12, color=text_color)
                
    # Remove axes
    ax.set_xticks(range(20))
    ax.set_yticks(range(10))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    # # Add colorbar with inverted colormap
    # if log_scale:
    #     cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap_func_r), 
    #                         ax=ax, pad=0.08, shrink=0.8)
    #     cbar.set_label('Mole Percent (Log Scale)', fontweight='bold')
    # else:
    #     cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap_func_r), 
    #                         ax=ax, pad=0.08, shrink=0.8)
    #     cbar.set_label('Mole Percent', fontweight='bold')
    # Add colorbar with inverted colormap - horizontal orientation at the bottom

    if log_scale:
        cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap_func_r), 
                            ax=ax, orientation='horizontal', pad=0.1, shrink=0.8)
        cbar.set_label('Mole Percent (Log Scale)', fontweight='bold')
    else:
        cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap_func_r), 
                            ax=ax, orientation='horizontal', pad=0.1, shrink=0.8)
        cbar.set_label('Mole Percent', fontweight='bold')
    # Set title
    plt.title(f'Elemental Mole Percent at Time Step {time_step}', fontweight='bold')
    
    # Save the figure with high DPI
    plt.tight_layout()
    plt.savefig(output_filename, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"Periodic table mole percent heatmap saved to {output_filename} at {dpi} DPI")

# Example usage
if __name__ == "__main__":
    plot_abundance_matplotlib(
        'Element_Vector.json',
        time_step=300,  # Specify which time step to visualize
        cmap='magma',  # or 'plasma', 'inferno', 'magma', 'cividis', 'turbo'
        log_scale=True,
        dpi=600  # High DPI for poster presentation
    )