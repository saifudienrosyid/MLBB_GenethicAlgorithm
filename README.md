# Final Project KKPM: GA Mobile Legend Team Composition

In this repository, we implement a genetic algorithm to recommend the best team composition.

## About Dataset
The MLBB Heroes dataset contains information related to role, health points, hero defense and many more. 

### Data Source

The dataset was obtained from [https://www.kaggle.com/datasets/kishan9044/](https://www.kaggle.com/datasets/kishan9044/mobile-legends-bang-bang).

### Data Description
This dataset consists of 18 attributes with 114 rows.
- **Name** : Names they are usually known by.
- **Title**: The Race of heroes. (Elf, Angel,Ninja, etc.)
- **Voice_Line**: Unique Voice line of each Hero.
- **Release_Date**: Official release date of the heroes on Original Server.
- **Primary_Role**: The main role of the hero.
- **Secondary_Role**: Hero is also suitable for this role. (if nan then no Secondary Role.)
- **Lane**: The play style of hero.
- **Hp**: Health of hero.
- **Hp_Regen**: Health Regeneration Rate of hero.
- **Mana**: Mana of Hero. (if nan then they dont use mana)
- **Mana_Regen**: Mana Regeneration Rate of hero.
- **Phy_Damage**: Basic Attack physical damage dealt by hero.
- **Magic_Damage**: Basic Attack Magic damage dealt by hero. (if o then the Basic Attack deals Physical Damage.)
- **Phy_Defence**: Physical Defence of hero.
- **Mag_Defence**: Magic Defence of hero.
- **Mov_Speed**: The movement speed of hero
- **Esport_Wins**: The number of games the hero has been picked by an E-sport team and they won the match.
- **Esport_Loss**: The number of games the hero has been picked by an E_sport team and they Lost the match.

## How to Use

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- Python 3
- Git

### Installation

_Follow this step to run our code._

1. Clone the repo
   ```sh
   git clone https://github.com/saifudienrosyid/MLBB_GenethicAlgorithm.git
   ```
2. Create new Python virtual environment in the folder
   ```py
   python -m venv .venv 
   ```
3. Install dependencies to virtual environment
   ```py
   pip install -r requirements.txt
   ```
4. Set .venv as a kernel to execute the code.
   ```py
   streamlit run app.py
   ```



## Authors

  - **Mufti Alfarokhul Azam** - [Email](mailto:muftialfarokhulazam@mail.ugm.ac.id)
  - **Saifudin Rosyid** -  [Email](mailto:saifudinrosyid@mail.ugm.ac.id)
  - **M. Al-Amin** - [Email](mailto:malamin@mail.ugm.ac.id)

## Acknowledgments

  - [kishan9044](https://www.kaggle.com/kishan9044) as the dataset provider
  - Inspiration