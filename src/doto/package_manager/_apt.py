# https://apt-team.pages.debian.net/python-apt/contents.html
# https://salsa.debian.org/apt-team/python-apt

import apt_pkg
import apt


def main():
    apt_pkg.init_config()
    apt_pkg.init_system()
    acquire = apt_pkg.Acquire()
    slist = apt_pkg.SourceList()
    # Read the list
    slist.read_main_list()
    # Add all indexes to the fetcher.
    slist.get_indexes(acquire, True)

    # Now print the URI of every item.
    for item in acquire.items:
        print(item.desc_uri)


if __name__ == "__main__":
    main()
