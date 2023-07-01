import qrcode

linkedin_porfile = "www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=sami-alashabi"

def make_qr_from_link(link: str=linkedin_porfile):
    """
    make a qr code from a link
    """
    if link:
        return qrcode.make(link)
    else:
        return qrcode.make(linkedin_porfile)