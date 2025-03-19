import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.colors import to_rgba
import matplotlib.colors as mcolors

def create_base_patterns():
    """Create a set of distinct patterns with increased density"""
    # Using doubled patterns for increased density
    return ['///', '---', '+++', 'xxx', 'ooo', 'OOO', '...', '***', '...', '+++', 'xxx']

# Function to get periodic table data (replacing the bokeh dependency)
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

def plot_surrogate_periodic_table(
    csv_file: str,
    output_filename: str = 'Surrogate_periodic_table.png',
    figsize: tuple = (20, 12)
):
    # Read the data
    elements = get_periodic_table_data()
    df = pd.read_csv(csv_file)
    
    # Get unique surrogates
    unique_surrogates = df['Surrogate'].dropna().unique()
    n_surrogates = len(unique_surrogates)
    
    # Generate colors for surrogates, ensuring specific elements get distinct colors
    base_colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#66CDAA', '#7f7f7f', '#bcbd22', '#17becf',  # Replaced '#e377c2' (pink) with '#66CDAA' (seafoam)
        '#a65628', '#f781bf', '#999999', '#e41a1c', '#377eb8',
        '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628'
    ]
    # Pre-allocate specific colors for problematic elements
    reserved_colors = {
        'Mo': '#d62728',  # Red
        'Ni': '#2ca02c',  # Green
        'Pd': '#9467bd',  # Purple
        'Kr': '#ff7f0e'   # Orange
    }
    
    # Replace the problematic code with this solution
    surrogate_colors = {}
    color_usage = {}
    assigned_colors = set()

    # First assign the reserved colors
    for surrogate in unique_surrogates:
        if surrogate in reserved_colors:
            surrogate_colors[surrogate] = reserved_colors[surrogate]
            assigned_colors.add(reserved_colors[surrogate])
            color_usage[reserved_colors[surrogate]] = 1

    # Then assign remaining colors
    for surrogate in unique_surrogates:
        if surrogate in surrogate_colors:
            continue
            
        # Find a color that hasn't been used yet if possible
        available_colors = [c for c in base_colors if c not in assigned_colors]
        if available_colors:
            color = available_colors[0]
        else:
            # If all colors are used, pick the least used one
            color = min(color_usage.items(), key=lambda x: x[1])[0]
        
        surrogate_colors[surrogate] = color
        assigned_colors.add(color)
        
        if color not in color_usage:
            color_usage[color] = 1
        else:
            color_usage[color] += 1
    
    # Create patterns for repeated colors
    patterns = create_base_patterns()
    # Assign patterns to surrogates with shared colors
    surrogate_styles = {}
    pattern_assignments = {}  # Track which patterns are used for each color

    for surrogate in unique_surrogates:
        color = surrogate_colors[surrogate]
        
        # Initialize pattern tracking for this color if needed
        if color not in pattern_assignments:
            pattern_assignments[color] = []
        
        # Only use pattern if this color appears multiple times
        if color_usage[color] > 1:
            # Find available patterns for this color
            used_patterns = pattern_assignments[color]
            available_patterns = [p for p in patterns if p not in used_patterns]
            
            if available_patterns:
                pattern = available_patterns[0]
            else:
                # If all patterns are used, cycle through them
                pattern_index = len(used_patterns) % len(patterns)
                pattern = patterns[pattern_index]
            
            pattern_assignments[color].append(pattern)
        else:
            pattern = None
        
        surrogate_styles[surrogate] = {
            'color': color,
            'pattern': pattern,
            'alpha': 0.9
        }
    
    # Create a special shared style for Br and Kr
    # First, ensure Kr has a style
    if 'Kr' not in surrogate_styles:
        surrogate_styles['Kr'] = {
            'color': reserved_colors['Kr'],
            'pattern': '///',
            'alpha': 0.9
        }
    
    # Use Kr's style for Br
    kr_style = surrogate_styles['Kr'].copy()
    surrogate_styles['Br'] = kr_style
    
    # Debug output
    print(f"Using identical style for Kr and Br: {kr_style}")
    
    # Use the same styles for elements as surrogates
    element_styles = surrogate_styles
    
    # Match quality colors
    match_quality_colors = {
        'self': '#000000',
        'Good': '#4CAF50',
        'Decent': '#FFA500',
        'Poor': '#FF0000'
    }
    
    # Create figure - adjust layout to accommodate vertical legend
    fig = plt.figure(figsize=figsize, facecolor='white')
    ax = fig.add_axes([0.05, 0.1, 0.7, 0.8])
    
    # Handle Lanthanides and Actinides
    lanthanides = [
        'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 
        'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'
    ]

    actinides = [
        'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 
        'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'
    ]

    # Plot elements
    for idx, row in elements.iterrows():
        symbol = row['symbol']
        
        try:
            group = int(row['group']) if row['group'] != 0 else None
            period = int(row['period']) if row['period'] != 0 else None
        except (ValueError, TypeError):
            group = None
            period = None

        if symbol in lanthanides:
            period = 8
            group = lanthanides.index(symbol) + 3  # Start at column 3
        elif symbol in actinides:
            period = 9
            group = actinides.index(symbol) + 3  # Start at column 3

        if group is not None and period is not None:
            # Special handling for Br and Kr to ensure they use the same style
            if symbol in ['Br', 'Kr']:
                # Get the shared style for Br and Kr
                shared_style = surrogate_styles['Kr']  # Use Kr's style as the reference
                element_color = shared_style['color']
                pattern = shared_style['pattern']
                alpha = shared_style['alpha']
                line_width = 1
                
                # Create element box with the shared style
                rect = Rectangle((group-0.5, period-0.5), 1, 1,
                               facecolor=element_color,
                               edgecolor='black',
                               linewidth=line_width,
                               alpha=alpha)
                ax.add_patch(rect)
                
                # Add pattern if needed
                if pattern:
                    ax.add_patch(Rectangle((group-0.5, period-0.5), 1, 1,
                                         hatch=pattern,
                                         fill=False,
                                         alpha=1.0,
                                         edgecolor='#333333'))
                
                # Add match quality indicator
                match_info = df[df['Symbol'] == symbol]
                if not match_info.empty:
                    match_quality = match_info['Match_Quality'].iloc[0]
                    if pd.isna(match_quality):
                        pass
                    elif isinstance(match_quality, str) and match_quality.lower() == 'self':
                        bar = Rectangle((group-0.4, period-0.4), 0.8, 0.05,
                                      facecolor=match_quality_colors['self'],
                                      edgecolor='none',
                                      linewidth=1)
                        ax.add_patch(bar)
                    else:
                        quality_str = str(match_quality)
                        quality_color = match_quality_colors.get(quality_str, 'gray')
                        indicator = Circle((group+0.3, period-0.3), 0.1,
                                        facecolor=quality_color,
                                        edgecolor='black',
                                        linewidth=1)
                        ax.add_patch(indicator)
                
                # Add element text
                ax.text(group, period, symbol,
                       ha='center', va='center',
                       fontweight='bold', fontsize=12,
                       color='black')
                
                ax.text(group, period+0.3, str(row['atomic number']),
                       ha='center', va='center',
                       fontsize=9, color='black')
                
                # Skip the regular element processing for Br and Kr
                continue
            
            # Regular element processing for all other elements
            element_data = df[df['Symbol'] == symbol]
            
            if not element_data.empty:
                surrogate = element_data['Surrogate'].iloc[0]
                match_quality = element_data['Match_Quality'].iloc[0]
                
                # Make elements without a match White
                if pd.isna(surrogate):
                    element_color = '#FFFFFF'
                    pattern = None
                    alpha = 0.9
                    line_width = 1
                else:
                    is_self = isinstance(match_quality, str) and match_quality.lower() == 'self'
                    if is_self:
                        style = surrogate_styles.get(surrogate, {})
                        element_color = style.get('color', '#CCCCCC')
                        pattern = style.get('pattern')
                        alpha = style.get('alpha', 0.9)
                        line_width = 2
                    else:
                        style = element_styles.get(surrogate, {})
                        element_color = style.get('color', '#CCCCCC')
                        pattern = style.get('pattern')
                        alpha = style.get('alpha', 0.9)
                        line_width = 1
                
                # Create element box with color
                rect = Rectangle((group-0.5, period-0.5), 1, 1,
                               facecolor=element_color,
                               edgecolor='black',
                               linewidth=line_width,
                               alpha=alpha)
                ax.add_patch(rect)
                
                # Add pattern with darker color and increased density
                if pattern:
                    ax.add_patch(Rectangle((group-0.5, period-0.5), 1, 1,
                                         hatch=pattern,
                                         fill=False,
                                         alpha=1.0,
                                         edgecolor='#333333'))
                
                # Add match quality indicators
                if pd.isna(match_quality):
                    pass
                elif isinstance(match_quality, str) and match_quality.lower() == 'self':
                    bar = Rectangle((group-0.4, period-0.4), 0.8, 0.05,
                                  facecolor=match_quality_colors['self'],
                                  edgecolor='none',
                                  linewidth=1)
                    ax.add_patch(bar)
                else:
                    quality_str = str(match_quality)
                    quality_color = match_quality_colors.get(quality_str, 'gray')
                    indicator = Circle((group+0.3, period-0.3), 0.1,
                                    facecolor=quality_color,
                                    edgecolor='black',
                                    linewidth=1)
                    ax.add_patch(indicator)

                # Add element text
                ax.text(group, period, symbol,
                       ha='center', va='center',
                       fontweight='bold', fontsize=12,
                       color='black')
                
                ax.text(group, period+0.3, str(row['atomic number']),
                       ha='center', va='center',
                       fontsize=9, color='black')

    # Set plot limits
    ax.set_xlim(-1, 20)
    ax.set_ylim(10, -1)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Create match quality legend with correct symbols
    match_quality_legend = [
        Rectangle((0, 0), 1, 0.05, facecolor=match_quality_colors['self'],
                 edgecolor='none', label='Self-representing'),
        Circle((0, 0), 0.1, facecolor=match_quality_colors['Good'],
               edgecolor='black', label='Good Match'),
        Circle((0, 0), 0.1, facecolor=match_quality_colors['Decent'],
               edgecolor='black', label='Decent Match'),
        Circle((0, 0), 0.1, facecolor=match_quality_colors['Poor'],
               edgecolor='black', label='Poor Match')
    ]
    
    # Create surrogate legend
    surrogate_legend = []
    
    # Create a list to track which surrogates we've already added to the legend
    added_to_legend = set()
    
    # Add the special Kr/Br entry first
    if 'Kr' in unique_surrogates:
        kr_style = surrogate_styles['Kr']
        surrogate_legend.append(Rectangle((0, 0), 1, 1, 
                               facecolor=kr_style['color'],
                               hatch=kr_style['pattern'] if kr_style['pattern'] else '',
                               alpha=kr_style['alpha'],
                               edgecolor='black',
                               label='Kr/Br'))
        added_to_legend.add('Kr')
        added_to_legend.add('Br')
    
    # Then add all other surrogates (except Kr and Br which we've already handled)
    for surrogate in unique_surrogates:
        if surrogate in added_to_legend:
            continue
            
        style = surrogate_styles[surrogate]
        patch = Rectangle((0, 0), 1, 1, 
                         facecolor=style['color'],
                         hatch=style['pattern'] if style['pattern'] else '',
                         alpha=style['alpha'],
                         label=f'{surrogate}')
        surrogate_legend.append(patch)
        added_to_legend.add(surrogate)
    
    # Add a legend for white (no match) elements
    surrogate_legend.append(Rectangle((0, 0), 1, 1, 
                              facecolor='white', 
                              edgecolor='black',
                              label='No Match'))
    
    # Add the match quality legend centered at the bottom
    match_legend = fig.legend(handles=match_quality_legend, 
                            loc='lower center',
                            title='Match Quality',
                            bbox_to_anchor=(0.4, 0.02),
                            ncol=4,
                            fontsize=15)
    # Make the title of the match quality legend larger
    match_legend.get_title().set_fontsize(17)
    
    # Add the surrogate legend on the right side, vertically stacked
    surrogate_legend = fig.legend(handles=surrogate_legend, 
                                 loc='center right',
                                 title='Surrogates',
                                 bbox_to_anchor=(0.85, 0.5),
                                 ncol=1,
                                 fontsize=15)
    # Make the title of the surrogate legend larger
    surrogate_legend.get_title().set_fontsize(17)
    
    plt.savefig(output_filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Surrogate periodic table saved to {output_filename}")

# Example usage
if __name__ == "__main__":
    plot_surrogate_periodic_table('PubChemElements_with_surrogates.csv')