from PIL import Image
import easyocr
import glob
import time
from natsort import natsorted


class EasyOCRSolver:
    def __init__(self):
        self.img_reader = easyocr.Reader(
            ["en"],
            gpu=True,
            verbose=False,
            model_storage_directory="../saved_models/model_dir/",       # set model_storage_directory here
            recog_network="best_accuracy",                              # set recog_network here
        )

    def ocr(
        self,
        path_img,
        ignore_alpha=False,
        ignore_digit=False,
        ignore_symbol=False,
        remove_new_line=False,
        max_len=False,
        min_len=False,
    ):
        try:
            text = str(self.img_reader.readtext(path_img)[0][1])
            if ignore_alpha:
                text = "".join([i for i in text if not i.isalpha()])
            if ignore_digit:
                text = "".join([i for i in text if not i.isdigit()])
            if ignore_symbol:
                text = "".join([i for i in text if i.isdigit() or i.isalpha()])
            if remove_new_line:
                text = "".join(text.split("\n"))
            if max_len:
                if len(text) > max_len:
                    return ""
            if min_len:
                if len(text) < min_len:
                    return ""
            return text
        except Exception as e:
            return False


easyocrSolver = EasyOCRSolver()


def solve_image(fname):
    im = Image.open(fname)
    im.save("_.png")
    text = chaptchaSolver.ocr(
        path_img="_.png",
        # ignore_alpha=True,                    # configure easyocr
        # ignore_digit=False,
        # ignore_symbol=True,
        # remove_new_line=True,
        # max_len=4,
        # min_len=4,
    )
    if text == False or text == "":
        return
    print(f" [!] Image: {text}\n")
    return text


def main():
    directory = "../all_data/en_custom"         # set en_custom to your ready to use dataset
    jpg_files = glob.glob(directory + "/*.jpg") # set format of the image
    sorted_jpg_files = natsorted(jpg_files)
    counter = 0
    for jpg_file in sorted_jpg_files:
        time.sleep(3)
        print("=" * 20)
        print(f"{counter} | Processing: {jpg_file}")
        counter += 1
        solver = solve_captcha(jpg_file)
        if solver is None or solver == "":
            print("...skipped")
            continue
        print("SOLVED: " + solver)


if __name__ == "__main__":
    main()
