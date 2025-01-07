import os


def check_file_presence(folder_list, dir_a, dir_b):
    missing_from_a = []
    missing_from_b = []

    # Iterate over each folder
    for folder in folder_list:
        # List all files in the current 'ori' folder
        try:
            files = os.listdir(folder)
            for file in files:
                file_path = os.path.join(folder, file)

                # Check if the file exists in My Mods-BR
                if not os.path.exists(os.path.join(dir_a, file)):
                    missing_from_a.append((file, folder))

                # Check if the file exists in My Mods' Backup
                if not os.path.exists(os.path.join(dir_b, file)):
                    missing_from_b.append((file, folder))
        except FileNotFoundError:
            print(f"Folder not found: {folder}")
        except Exception as e:
            print(f"An error occurred for folder {folder}: {e}")

    return missing_from_a, missing_from_b


def main():
    folder_list = [
        r"G:\PSO_Stuff\Working\InProgress\AiryariaB2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Bunny Suit [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Alpha + Beta\ori",
        r"G:\PSO_Stuff\Working\InProgress\Alva Spiagnia V2B [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Anemos Delsolab2\ori",
        r"G:\PSO_Stuff\Working\InProgress\Aristo BroderieB [Se]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Arte Servine D + V2\ori",
        r"G:\PSO_Stuff\Working\InProgress\Attentater T2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Bunk Mesher T2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Cheers LitB [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Craw Swimmer B2\ori",
        r"G:\PSO_Stuff\Working\InProgress\Fascina DiavolaB [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Fearal Cat4 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Forte MaestronaB [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Lapin Rapid3 V2 V3[Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Lightie SavelgeC [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Loosse Ceinture [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Lumier SnauticaB2 [Se]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Matsukai Mao Replica V2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Chocolat Felice V2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Combat Jacket T2 +T2B\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Forge Line2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Hariette BattlewearB [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Holy PhantasmC [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Joyous\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Micro Mini Shorts V2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Nocturnal Mists T2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Thousand Rim\ori",
        r"G:\PSO_Stuff\Working\InProgress\N-Wedding Dress [Se] + 2\ori",
        r"G:\PSO_Stuff\Working\InProgress\Nacht Tiger T22 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Natalis RochkaC [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Riconizza NebilaB [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Ryza's Outfit V2B + B\ori",
        r"G:\PSO_Stuff\Working\InProgress\Santisse Marina V2 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Sirena Abysal [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Spyder T2 B[Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Stregati B V2B\ori",
        r"G:\PSO_Stuff\Working\InProgress\Sunny PuryB [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Sylphy Conifer2\ori",
        r"G:\PSO_Stuff\Working\InProgress\Urban Night V4 [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Vayarge Marinetta [Ba]\ori",
        r"G:\PSO_Stuff\Working\InProgress\Vestia Seerea V2B [Ba]\ori"

    ]

    dir_a = r"C:\\Users\\Draconian\\Desktop\\PSO2 Mods\\My Mods-BR"
    dir_b = r"C:\\Users\\Draconian\\Desktop\\Main Backup\\My Mods' Backup"

    missing_from_a, missing_from_b = check_file_presence(folder_list, dir_a, dir_b)

    if missing_from_a:
        print("Missing from My Mods-BR:")
        for file, folder in missing_from_a:
            print(f"{file} from {folder}")
    else:
        print("No files missing in My Mods-BR.")

    if missing_from_b:
        print("Missing from My Mods' Backup:")
        for file, folder in missing_from_b:
            print(f"{file} from {folder}")
    else:
        print("No files missing in My Mods' Backup.")

if __name__ == "__main__":
    main()
