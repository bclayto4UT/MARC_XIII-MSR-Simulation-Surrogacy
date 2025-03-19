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
- A Breif Introduction to the EIRENE CYCLE, including a discussion/acknowledgment of the use of percribed seperations methods.

## More on Mapping
- Insert Mapping Explination here, Include Graphic with MSTDB Data Availability, explain how each addition to the database is increasingly complex

## S'more Findings 
- Explain initial findings on redox control and UF3 deposition

## Hopes for the Future
- Go into a little more depth about plans and next steps, discuss how this tool will adi multiphysics assesments of the core. 
