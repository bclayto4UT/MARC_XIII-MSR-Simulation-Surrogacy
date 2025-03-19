# MARC_XIII-MSR-Simulation-Surrogacy
An Introduction to a methodology for the more complete representation of MSR lifecycle chemistry, as presented at the 2025 International Conference on Methods and Applications of Radioanalytical Chemistry under Log # 335: THE DESIGN AND DEMONSTRATION OF A SIMULATION SURROGACY METHOD FOR THE STUDY OF MSR LIFECYCLE CHEMISTRY

## Welcome
Thank you for your intrest! Regardless of if you are a confrence atendee who found this poster, or a curious individual who stumbled across this repository another way, we are excited to share with you some of our work.

### Asking Qustions or Giving Comments? 

We are eager to get your feedback as we try to build useful tools for the exploration of Molten Salt Reactor Chemistry.

**Some Specific Areas we are Looking for Feedback** 
- How Can We Improve Our Surrogacy Mapping? 
- What nuclides and elements are most important to your work? 
- Are there specific chemical behaviors, or operations schemes you are interested in?

If you can answer any of these questions, have questions of your own or have any other feedback we invite you to use the Issues board to share it all with us.

To do this, create an Issue, be sure to include your name and contact info if you would like a direct response rather than a comment on the issue board. Feel free to atach any materials that may be helpful in our discusions. However, do realize that this is a public repository and that information shared on the issue board can be read by any who access it.

If you would rather, feel free to contact the primary author (Braden Clayton) via email: bkc959@my.utexas.edu

### Navigating the Repository

There is a lot here, we want to avoid you getting lost.

- Poster Materials, poster graphics and some great graphics we couldnt squeze into the posters are in the primary directory, these include:
   - `Main_Poster.pdf`
   - `Bonus_Poster.pdf`
   - .
   - .
   - .
- Code for the Surrogate Mapping can be found in `SURROGATE_MAPPING_GEN_I`, incuding detailed explanations of each file present.
- The Workhorse code can be found in `SCALE_2_THERMOCHIMICA`, which also has an explination of the code, its use and dependencies. It is worthwhile to note that this code is writen to work on the Authors Laptop and has not been "Cleaned Up" for general use. If you would like to use it, be concious of paths to your Thermochimica Instalation. 
- `Additional_Materials` is for anyone who loves looking at graphs. It contains all the outputs of runs for a variety of fuel cycles.

### Additional Acknowledgments 

Again, a big thanks to the state of Texas for their support of the Molten Salt Reactor Digital Twin Initiative.

This work would not be possible if it were not for those building the tools we use, so another thank you for them:
- [Thermochimica](https://github.com/ORNL-CEES/thermochimica)
- [Molten Salt Thermochemical Database](https://mstdb.ornl.gov/)
- [Scale](https://www.ornl.gov/scale)

A particular thank you is in order for co-authors:
- **Loc Duong** - Whose pionering efforts in Molten Salt Chemistry work here at UT Austin while he was an undergrad, paved the way for the development of these tools. [Loc's Original Scale to Thermochimic Code](https://github.com/lduong1/msr-fission-gas)
-  **C. Erika Moss** - For her work on the EiRENE Fuel Cycle and her willingness to help process scale outputs. [See her repository here](https://github.com/cerikam/IMSR) 

The Author also found the following repositories helpful in the creation of these tools:
- [periodic_trends](https://github.com/Andrew-S-Rosen/periodic_trends)


### Citations

We hope to publish a portion of this work in a journal in the near future. Once we have we will provide the approiate citation. Until then, please contact Braden directly if you are interested in using any of this work.

---------

# Introducing the Molten Salt Reactor Digital Twin Initiative

## About

### Next Generation Energy
Nuclear energy is a strong candidate to supplement fossil fuels, with molten salt reactors (MSRs) offering key advantages in safety, sustainability, energy security, and waste management. MSRs operate at atmospheric pressure with liquid fuel, making them inherently safer than traditional high-pressure, solid-fuel reactors.

The Nuclear Regulatory Commission (NRC) requires vast amounts of safety data, traditionally taking decades to gather. Digital modeling tools can accelerate safe design progress and continuous reactor innovation.

## Texas Solution
Texas is driving MSR development through collaborative efforts between industry and academia. Abilene Christian University (ACU) is constructing a research reactor, with plans for more across the state. The Digital Molten Salt Reactor Initiative will:

- Create a digital twin reactor to improve digital modeling accuracy.
- Deploy sensors and simulations to validate predictive models.
- Model experimental salt corrosion and chemistry impacts.
- Build a digital grid model to show MSRs' contribution to energy reliability.

This will promote innovation and safety, following the example of U.S. leadership in technology and aviation.

## Why UT Austin?
UT Austin is well-equipped to lead this initiative, leveraging:

- **Texas Advanced Computing Center**: A global leader in high-performance computing.
- **Oden Institute**: Expertise in computational science and engineering.
- **Energy Institute**: Research on the energy economy.
- **NETL Reactor**: The newest U.S. research reactor.

### Mission
Demonstrate how digital twins (DTs) can enable regulatory approval and innovation in nuclear and molten salt systems.

### Vision
Position UT Austin as the top university for digital twin R&D in advanced reactor technologies.

### Colabortion
We are always looking to colaborate, if you are interested in exploring colaboration feel free to contact Dr. Kevin Clarno clarno@utexas.edu or Dr. Derek Haas derekhaas@utexas.edu

---------
# A Deeper Dive Into The Poster

When excited about a topic, creating a poster can be a grueling effort in acedemic minimalisim. In other words, there is never enough space. The folloowing section include thoughts and explinations that simply did not fit on the board.

## Introduction

## The EIRINE Cycle

The EIRENE and ThEIRENE reactor models serve as versatile, open-source platforms for exploring advanced molten salt reactor fuel cycles, with a focus on education and research. EIRENE, inspired by the IMSR-400 design, utilizes high-assay low-enriched uranium (HALEU) fuel in a liquid salt medium and is designed to demonstrate innovative fuel cycle strategies like the Sourdough refueling approach, enabling continuous salt rejuvenation and extended reactor operation. Building on this foundation, the ThEIRENE model introduces a fertile thorium and fissile HALEU fuel mixture, offering a pathway to explore sustainable, closed fuel cycles with significant potential for breeding new fissile material and reducing long-term radiotoxic waste. Together, these models provide a comprehensive framework for assessing neutronic behavior, temperature feedback, depletion characteristics, and advanced fuel cycle performance in next-generation molten salt reactors.

These Fuel Cycles employ somewhat arbitrary seperation schemes, periodicly/consistently pulling noble metals and Gases from the salt phase. They do not include any consideration for Redox Control. 

## More on Mapping
Though the MSTDB has collected a large amount of Data, and has made sigificant improvments in just the last 2 years, there are still many elements not represented in the database:

#### Version 3.0
Simplification of Information presented here: 
![image](https://github.com/user-attachments/assets/24ba133a-959d-48ef-be67-77d10f295e6f)

For studies, such as fuel and lifecycle chemistry, it is important to have a more comprehensive view of salt chemistry than is currently possible with this selection. That is where simulation surrogates come in. Similar to how a chemist can substitute Pu for a chemicaly similar element, we intend to substiture elements for which there is no data with surrogates who have data present and available.

### Proposed Approach (Gen_0/1)

This Approach was drafted as a first attempt. Commentary on more ideal methodologies and what will be required to implement them will be given in the results portion of this report.

#### Terminology:

**Surrogate** - The Element present in MSTDB-TC which is to be used to represent itself and other elements not present in the database

**Candidate** - An Element not present in MSTDB-TC which will be represented by a Surrogate

***

**Goal:** To Map the entirety of the periodic table to those elements available in MSTDB-TC. This will allow for a more complete, though inherently imperfect, representation of Molten Salt behavior. This more complete method will be used to build the Digital Twin frameworks so that when more accurate data become available the accuracy of these frameworks can be improved rapidly without need for a major overhaul.

#### Methodology 

1. Compare Valance States with available data for Standard Potential of ion formation half reactions. "Perfect matches" would be those who have the same available half reactions and whose standard potentials for each nearly match.  

2. Baring a "Perfect Match", we would then compare the half reaction of greatest potential, for example if Candidate X has a 4+, and a 2+ reaction, and the proposed surrogate S has a 2+, 1+ reaction, but the 2+ reaction of both has the greatest potential, and that potential is similar, then these will be considered an appropriate match. 

3. If a given Candidate has no match under the previous descriptions, there are three options available: 1) Match based on similar Electronegativity, 2) Match Based on Similar Melting Point(Elemental), 3) Determine that there is no available match.

4. Eliminate those elements who have No Suitable Surrogate available (Hydrogen, Oxygen and other non-halogen Pblock elements)

#### "Accuracy Assessment"

Out of an interest in determining the "accuracy" or how justifiable a given paring is the following assessment is suggested. 

* Each Pairing of a Candidate with a surrogate will be given a score:

   1 - Good Paring (Meets Conditions in Methodology step 2.)

   2 - Decent Paring (Meets Conditions in Methodology step 3.)

   3 - Poor Paring (Meets Conditions in Methodology step 4.)

* Some Key Metrics Relating to Chemical Similarity will also be recorded
   * Difference between greatest/most matched Standard Potential of Candidate and Surrogate
   * Electronegativity
   * Electron Affinity
   * Melting Point

#### Justifications
One of the obvious flaws of this methodology is the use of standard potentials vs at-temperature potentials. The reasoning for this is two fold:

1. This is an attempt to make a general mapping methodology that is independent of fuel cycle and/or general salt composition. As finding the actual potential requires simulation specific data such as temperature and concentrations, it would be preferable to use the constant standard potentials instead. 

2. According to the nernst equation, potential scales linearly with temperature.  Thus so long as reactions are of the same valency, the difference between standard potentials will be the same as the difference between actual potentials. Because this mapping is primarily based on the difference in potentials between similar reactions, we assume our use of standard potentials to be reasonable. 

There remains one flaw that is not addressed; reactions with differing amounts of electrons scale with at different rates. In many of these mappings only the highest valence state is considered. If there are substantial differences between surrogate and candidate in other valence states, these differences may become more significant at higher temperatures, the pairings may be invalid above certain temperature thresholds. This will be discussed more in future work.

A second apperant flaw of this proposed approach is the use of elemental properties as opposed to fluoride properties. As will be shown in the results section, most poor pairings that would use this logic are considered to be invalid, thus this inaccuracy has little impact on the actual mapping. Considerations for the inclusion of Fluoride properties and the reasoning for why they were not included in this iteration will be given in future work.  

##### Explanation of the Nernst Equation for a Half-Cell Reaction

The Nernst equation is used to calculate the reduction potential of a half-cell in an electrochemical cell. It is given by:

$$E = E^0 - \frac{RT}{nF} \ln Q_r $$

Where:
- \( E \) is the reduction potential of the half-cell.
- \( E^0 \) is the standard reduction potential.
- \( R \) is the universal gas constant (8.314 J/mol·K).
- \( T \) is the temperature in Kelvin.
- \( n \) is the number of moles of electrons transferred.
- \( F \) is the Faraday constant (96485 C/mol).
- \( Q_r \) is the reaction quotient.

The reaction quotient (\( Q_r \)), also often called the ion activity product (IAP), is the ratio between the chemical activities (\( a \)) of the reduced form (the reductant) and the oxidized form (the oxidant). The chemical activity of a dissolved species corresponds to its true thermodynamic concentration, taking into account the electrical interactions between all ions present in solution at elevated concentrations. For a given dissolved species, its chemical activity (\( a \)) is the product of its activity coefficient (\( \gamma \)) and its molar (mol/L solution) or molal (mol/kg water) concentration (\( C \)): \( a = \gamma C \).

So, if the concentration (\( C \), also denoted below with square brackets [ ]) of all the dissolved species of interest is sufficiently low and their activity coefficients are close to unity, their chemical activities can be approximated by their concentrations as commonly done when simplifying, or idealizing, a reaction for didactic purposes:

$$ Q_r = \frac{a_{\text{Red}}}{a_{\text{Ox}}} = \frac{[\text{Red}]}{[\text{Ox}]} $$


(This section was taken from Wikipedia and is included here for easy reference) 
***

### Results 
(Note: These Results Should be Considered Gen_0 Mapping, the Map included in the poster is an improved version of this, simply removing elements with complete incompatabilities)

#### Graphical Representation of Elemental Mapping 
![Surrogate_periodic_table2](https://github.com/user-attachments/assets/86607e2f-c460-4dd6-b477-b939d7479716)

In this graphic elements present in MSTDB-TC are denoted by a black bar. The candidates that pertain to each of these potential surrogates are colored with lighter shade of the surrogates color and share the same pattern. Each candidate is flagged according to the accuracy of their pairing. It is important to note that though this graphic shows p-block elements such as B, C, N, O, Si, P as well as H as having surrogates, these are considered to be invalid parings. Future versions of this graphic will exclude them entirely.  
#### Elemental Mapping Report 
The Surrogates and their Candidates are summarized in this json file. A more complete report can be found bellow. 

<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">

<head>

<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 15">
<link id=Main-File rel=Main-File
href="file:///C:/Users/brade/AppData/Local/Temp/msohtmlclip1/01/clip.htm">
<link rel=File-List
href="file:///C:/Users/brade/AppData/Local/Temp/msohtmlclip1/01/clip_filelist.xml">
<style>
<!--table
	{mso-displayed-decimal-separator:"\.";
	mso-displayed-thousand-separator:"\,";}
@page
	{margin:.75in .7in .75in .7in;
	mso-header-margin:.3in;
	mso-footer-margin:.3in;}
tr
	{mso-height-source:auto;}
col
	{mso-width-source:auto;}
br
	{mso-data-placement:same-cell;}
td
	{padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:"Aptos Narrow", sans-serif;
	mso-font-charset:0;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;
	mso-protection:locked visible;
	white-space:nowrap;
	mso-rotate:0;}
.xl65
	{vertical-align:middle;
	white-space:normal;}
-->
</style>
</head>

<body link="#467886" vlink="#96607D">

Sur.|Candidates
-- | --
Ru | H (Poor), P (Poor),  Os (Poor)
He |  
Li |  
Be | V (Decent), Mn (Decent), In   (Decent), Pr (Decent), Pm (Decent), Dy (Decent), Ho (Decent), Er (Decent), Bk   (Decent), Cf (Decent), No (Decent)
Mo | B (Poor), As (Poor), Nb   (Decent), Sb (Poor), Te (Poor), Ta (Good), W (Good), Re (Decent), Ir (Decent)
Xe | C (Poor), S (Poor), Xe (self)
Kr | N (Poor), Kr (self)
Cl | O (Poor), Cl (self), Br (Good), Rn (Poor)
F | F (self)
Ne | Ne (self)
Na | Na (self)
Sr | Mg (Decent), Ca (Good),
Cr | Al (Decent), Ti   (Decent),  Co (Decent), Cu (Decent), Ge   (Decent), Sn (Decent), Bi (Decent), Pa (Decent), Am (Decent), Cm (Decent)
Tc | Si (Poor)
Ar |  
K | Fr (Good)
Ce | Sc (Good), Gd (Good), Lu   (Good), Ac (Good), Lr (Good)
Fe | Au (Decent)
Ni | Zn (Decent), Cd (Good), Pb   (Good), Po (Poor)
Rh | Ga (Decent),  Ag (Decent), Tl   (Decent)
I | Se (Decent),  At (Decent)
Rb |  
La | Y (Good), Tb (Decent)
Zr | Hf (Good)
Pd | Pt (Good), Hg (Good)
Cs |  
Ba | Ra (Good)
Nd | Sm (Decent), Eu (Good), Yb (Decent), Es (Decent), Fm (Decent), Md   (Decent)
Pu | Tm (Poor)
Th |  
U | Np (Decent)



</body>

</html>


[surrogates_and_candidates.json](https://github.com/user-attachments/files/18946891/surrogates_and_candidates.json)

[[See Full Mapping Report Here]]

 

#### Next Steps: Improved Methodologies, Barriers and Important Assessments

Any experienced chemist should immediately spot many holes in this methodology. These include the use of standard potential vs potentials at the appropriate temperatures, the lack of information on Fluoride specific reactions, and an incomplete representation of possible valencies for many elements. It is important to remember that a complete thermochemical representation of each element would eliminate the need for these approximations. Thus in the absence of a complete database there will always be inherent inaccuracy in any approximation. That said, there are more appropriate approximations that might be made if good data can be found. This section of the report presents a few methods we continue to explore which may improve the elemental mapping.

**1. Temperature Dependence** 
The behavior of each of these surrogates and their candidates is highly dependent on system temperature. A more robust methodology would dynamically adjust these pairings based on a given temperature for each simulation. This could easily be implemented if we continue to use the potentials of half reactions as we have done here and define expected concentrations for each reaction. The primary reason this was not done from the start was an interest in creating a mapping that could be used independent from system specific criteria.

**2. Energy of Formation**
One of the reasons for the use of the standard potentials is that the calculation of these standards is based on Gibs Free Energy. Perhaps a superior methodology would focus directly on Gibbs Free Energy of Formation for each Floride of interest. Grouping could be done using two criteria, similar gibbs free energy of formation, and matching valency. Valency would still need to be considered because part of the need for these approximations is to more accurately model the redox drift of the salt caused by fuel consumption. Representing an element X who is a tetra-fluoride as a tri-fluoride would skew the results of such a study. 

The primary reason for not including this yet is the scarcity of data for many of the needed fluorides. If we had all the needed values, we could create a far more thorough database. That said, we continue to look for data so that we may begin exploring this option.   

**3. Fluoride Specific Data**  
The physical characteristics of elements, such as melting point, can only hint at how the element might behave. However, if we had this information for the various fluorides we are interested in it may prove a more effective method for grouping. This data is generally easier to find than complete thermochemical data (Entropies and Enthalpies). This was not done from the start as I could find no comprehensive list of fluoride properties but the elemental information was readily available. 

Each of these methods are dependent on better data. We continue to look for that data, and as we find it plan to update the grouping methodology as needed. 

Another item that will be of interest to the eventual publication of these methodologies is the inclusion of an assessment of the relative importance of those elements not yet found in the MSTDB-TC. This Assessment could examine each element based on expected abundance in the fuel cycle, possible hazards to health if released, and retaliative neutronic impact. This will help inform us of what expansions to the MSTDB-TC are most needed. 
***
### Sources and Supplementary Material 
Included in this appendix are the half reactions and code used to perform the mapping, as well as some useful graphics. 
#### Half-Reactions 
[electrochemical series.pdf](https://github.com/user-attachments/files/18771192/electrochemical.series.pdf)

## S'more Findings 
- Explain initial findings on redox control and UF3 deposition

## Hopes for the Future
- Go into a little more depth about plans and next steps, discuss how this tool will adi multiphysics assesments of the core. 
