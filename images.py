from PIL import Image

badge = Image.open("nyan_tr.gif")


def convert_image_with_vote(image, vote):
    return _convert_image_to_no(image)


def _convert_image_to_no(image):
    profile = Image.open(image)

    profile_box = profile.getbbox()
    badge_box = badge.getbbox()

    box = (profile_box[2] - badge_box[2], profile_box[3] - badge_box[3])
    profile.paste(badge, box, badge)
    return profile

def _convert_image_to_yes(image):
    raise NotImplementedError('Not a chance!')
