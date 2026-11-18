import sys
import subprocess

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QWidget, QHeaderView, QAbstractItemView,
    QPushButton, QMessageBox, QLabel
)

softwarelist = [
    ["gnome-screenshot", "screenshot application for GNOME", "https://wiki.gnome.org/Apps/Attic/GnomeUtils"],
    ["flameshot", "Powerful yet simple-to-use screenshot software", "https://flameshot.org"],
    ["magnus", "Very simple screen magnifier", "https://github.com/stuartlangridge/magnus"],
    ["gcolor3", "Simple GTK3 color selector and picker", "https://github.com/Hjdskes/gcolor3"],
    ["gpick", "advanced GTK+ color picker", "http://www.gpick.org"],
    ["kcolorchooser", "color chooser and palette editor", "https://apps.kde.org/kcolorchooser"],
    ["lximage-qt", "Image viewer for LXQt", "https://github.com/lxqt/lximage-qt"],
    ["shotwell", "digital photo organizer", "https://wiki.gnome.org/Apps/Shotwell"],
    ["gimp", "GNU Image Manipulation Program", "https://www.gimp.org/"],
    ["krita", "pixel-based image manipulation program", "https://krita.org/"],
    ["gnome-paint", "", ""],
    ["kolourpaint", "simple image editor and drawing application", "https://apps.kde.org/kolourpaint/"],
    ["mtpaint", "painting program to create pixel art and manipulate digital photos", "https://mtpaint.sourceforge.net/"],
    ["kruler", "screen ruler", "https://apps.kde.org/kruler/"],
    ["inkscape", "vector-based drawing program", "https://inkscape.org"],
    ["blender", "Very fast and versatile 3D modeller/renderer", "https://www.blender.org/"],
    ["qtqr", "Qt frontend for QR code generator and decoder", "https://launchpad.net/qr-tools"],

    ["nano", "small, friendly text editor inspired by Pico", "https://www.nano-editor.org/"],
    ["gnome-calculator", "GNOME desktop calculator", "https://apps.gnome.org/Calculator/"],
    ["libreoffice-writer", "office productivity suite -- word processor", "http://www.libreoffice.org"],

    ["make", "utility for directing compilation", "https://www.gnu.org/software/make/"],
    ["automake", "Tool for generating GNU Standards-compliant Makefiles", "https://www.gnu.org/software/automake/"],
    ["geany", "fast and lightweight IDE", "http://www.geany.org"],
    ["geany-plugins-common", "set of plugins for Geany (translations)", "http://plugins.geany.org"],
    ["featherpad", "lightweight plain-text editor written in Qt", "https://github.com/tsujan/featherpad"],
    ["python3-all", "package depending on all supported Python 3 runtime versions", "https://www.python.org/"],
    ["python3-pynput", "control and monitor input devices (Python 3)", "https://github.com/moses-palmer/pynput"],
    ["xdotool", "simulate (generate) X11 keyboard/mouse input events", "https://github.com/jordansissel/xdotool/"],
    ["python3-pyqt6", "Python bindings for Qt 6", "https://riverbankcomputing.com/software/pyqt/intro"],
    ["python3-webview", "Build GUI for your Python program with JavaScript, HTML, and CSS", "https://github.com/r0x0r/pywebview"],
    ["python3-wheel", "built-package format for Python", "https://github.com/pypa/wheel"],
    ["apache2", "Apache HTTP Server", "https://httpd.apache.org/"],
    ["zeal", "Simple offline API documentation browser", "https://zealdocs.org/"],
    ["kdevelop", "integrated development environment for C/C++ and other languages", "https://www.kdevelop.org/"],
    ["kdevelop-php", "PHP plugin for KDevelop", "https://www.kdevelop.org/"],
    ["kdevelop-python", "Python 3 plugin for KDevelop", "https://www.kdevelop.org/"],
    ["ghex", "GNOME Hex editor for files", "https://wiki.gnome.org/Apps/Ghex"],
    ["gnome-builder", "IDE for GNOME", "https://apps.gnome.org/Builder/"],
    ["cmake", "cross-platform, open-source make system", "https://cmake.org/"],
    ["wine", "Windows API implementation - standard suite", "https://www.winehq.org"],

    ["grub-customizer", "GUI to configure GRUB2 and BURG", "https://launchpad.net/grub-customizer"],
    ["plymouth-themes", "boot animation, logger and I/O multiplexer - themes", "https://www.freedesktop.org/wiki/Software/Plymouth"],
    ["adwaita-icon-theme","", "https://gitlab.gnome.org/GNOME/adwaita-icon-theme"],
    ["adwaita-icon-theme-legacy","", "https://gitlab.gnome.org/GNOME/adwaita-icon-theme"],
    ["gnome-colors", "set of GNOME icon themes", "https://code.google.com/p/gnome-colors/"],
    ["gnome-extra-icons", "Optional GNOME icons - /usr/share/pixmaps", "http://art.gnome.org/"],
    ["gnome-icon-theme", "This package contains the default icon theme used by the GNOME", ""],
    ["qt5ct", "Qt5 Configuration Utility", "https://sourceforge.net/projects/qt5ct/"],
    ["qt6ct", "Qt6 Configuration Tool", "https://github.com/ilya-fedin/qt6ct"],
    ["darkcold-gtk-theme", "dark GTK2/GTK3/Metacity theme", "https://github.com/originalseed/darkcold"],
    ["gnome-themes-extra", "Adwaita GTK 2 theme — engine", "https://packages.fedoraproject.org/pkgs/gnome-themes-extra/gnome-themes-extra/"],

    ["lxterminal", "LXDE terminal emulator", "https://www.lxde.org/"],
    ["balena-etcher", "Flash OS images to SD cards and USB drives", "https://github.com/balena-io/etcher"],
    ["xfce4-taskmanager", "process manager for the Xfce4 Desktop Environment", "https://docs.xfce.org/apps/xfce4-taskmanager/start"],
    ["xfce4-terminal", "Xfce terminal emulator", "https://docs.xfce.org/apps/terminal/start"],
    ["synaptic", "Graphical package manager", "https://github.com/mvo5/synaptic/wiki"],
    ["gnome-terminal", "GNOME terminal emulator application", "https://wiki.gnome.org/Apps/Terminal"],
    ["gnome-system-monitor", "Process viewer and system resource monitor for GNOME", "https://apps.gnome.org/SystemMonitor/"],
    ["pcmanfm", "extremely fast and lightweight file manager", "https://github.com/lxde/pcmanfm"],
    ["thunar", "File Manager for Xfce", "https://docs.xfce.org/xfce/thunar/start"],
    ["p7zip-full", "transitional package", "https://7-zip.org/"],
    ["lxqt-archiver", "Archiv Manager for LXQt", "https://github.com/lxqt/lxqt-archiver"],
    ["fsearch", "Fast graphical file search utility", "https://cboxdoerfer.github.io/fsearch/"],
    ["catfish", "File searching tool which is configurable via the command line", "https://docs.xfce.org/apps/catfish/start"],
    ["k4dirstat", "graphical disk usage display with cleanup facilities", "https://github.com/jeromerobert/k4dirstat"],
    ["baobab", "GNOME disk usage analyzer", "https://apps.gnome.org/Baobab/"],
    ["gpart", "Guess PC disk partition table, find lost partitions", "https://github.com/baruch/gpart"],
    ["gparted", "GNOME partition editor", "https://gparted.org"],
    ["xfburn", "CD-burner application for Xfce Desktop Environment", "https://docs.xfce.org/apps/xfburn/start"],
    ["bleachbit", "delete unnecessary files from the system", "https://www.bleachbit.org/"],
    ["caffeine", "prevent the desktop becoming idle in full-screen mode", "https://launchpad.net/caffeine"],
    ["conky-std", "highly configurable system monitor (default version)", "https://github.com/brndnmtthws/conky"],
    ["nemo", "file manager and graphical shell for Cinnamon", "http://www.github.com/linuxmint/nemo/"],

    ["lxmusic", "LXDE music player", "http://www.lxde.org/"],
    ["audacious", "small and fast audio player which supports lots of formats", "https://www.audacious-media-player.org/"],
    ["mixxx", "Digital Disc Jockey Interface", "https://www.mixxx.org/"],
    ["audacity", "fast, cross-platform audio editor", "https://www.audacityteam.org/"],
    ["mp3splt-gtk", "split MP3, Ogg Vorbis, or FLAC files without re-encoding", "http://mp3splt.sourceforge.net/"],
    ["lame", "MP3 encoding library (frontend)", "https://lame.sourceforge.io/"],
    ["lmms", "Linux Multimedia Studio", "https://lmms.io/"],
    ["hydrogen", "advanced drum machine/step sequencer", "http://www.hydrogen-music.org/"],
    ["tuxguitar", "Multitrack guitar tablature editor and player", "https://www.tuxguitar.app"],
    ["muse", "Qt-based audio/MIDI sequencer", "https://muse-sequencer.github.io/"],
    ["qjackctl", "User interface for controlling the JACK sound server", "https://qjackctl.sourceforge.io"],
    ["rakarrack", "Simple and easy guitar effects processor for GNU/Linux", "http://rakarrack.sourceforge.net"],
    ["guitarix", "Rock guitar amplifier for JACK", "https://guitarix.org"],

    ["mediainfo-gui", "graphical utility for reading information from audio/video files", "https://mediaarea.net/MediaInfo"],
    ["ffmpeg", "Tools for transcoding, streaming and playing of multimedia files", "https://ffmpeg.org/"],
    ["obs-studio", "recorder and streamer for live video content", "https://obsproject.com"],
    ["kazam", "screencast and screenshot application created with design in mind", "https://launchpad.net/kazam"],
    ["simplescreenrecorder", "Feature-rich screen recorder for X11 and OpenGL", "https://www.maartenbaert.be/simplescreenrecorder/"],
    ["gnome-video-trimmer", "Simple GUI application for lossless cutting of video files", "https://apps.gnome.org/VideoTrimmer/"],
    ["kdenlive", "non-linear video editor", "https://kdenlive.org/"],
    ["handbrake", "versatile DVD ripper and video transcoder (GTK+ GUI)", "https://handbrake.fr/"],
    ["winff", "graphical video and audio batch converter using ffmpeg or avconv", "https://github.com/WinFF/winff"],
    ["vlc", "multimedia player and streamer", "https://www.videolan.org/vlc/"],
    ["totem", "Simple media player for the GNOME desktop based on GStreamer", "https://wiki.gnome.org/Apps/Videos"],
    ["celluloid", "simple GTK+ frontend for mpv", "https://github.com/celluloid-player/celluloid"],
    ["mplayer-gui", "movie player for Unix-like systems (GUI variant)", "https://mplayerhq.hu"],
    ["kmplayer", "media player for KDE", "https://kmplayer.kde.org"],
    ["mpv", "video player based on MPlayer/mplayer2", "https://mpv.io/"],

    ["gufw", "graphical user interface for ufw", "https://costales.github.io/projects/gufw/"],
    ["firefox", "The Mozilla Firefox web browser", "https://github.com/mozilla-firefox/firefox"],
    ["thunderbird", "mail/news client with RSS, chat and integrated spam filter support", "https://www.thunderbird.net/"],
    ["epiphany-browser", "Intuitive GNOME web browser", "https://apps.gnome.org/Epiphany/"],
    ["claws-mail", "Fast, lightweight and user-friendly GTK based email client", "https://www.claws-mail.org/"],
    ["gnome-maps", "map application for GNOME", "https://apps.gnome.org/Maps/"],
    ["transmission", "lightweight BitTorrent client", "https://transmissionbt.com/"],
    ["pitivi", "non-linear audio/video editor using GStreamer", "https://www.pitivi.org"],
    ["freetuxtv", "Internet television and radio player", "https://github.com/freetuxtv/freetuxtv"],
    ["webhttrack", "Copy websites to your computer, httrack with a Web interface", "https://www.httrack.com/"],

    ["aisleriot", "GNOME solitaire card game collection", "https://wiki.gnome.org/Apps/Aisleriot"],
    ["gnome-mahjongg", "classic Eastern tile game for GNOME", "https://wiki.gnome.org/Apps/Mahjongg"],
    ["gnome-chess", "simple chess game", "https://wiki.gnome.org/Apps/Chess"],
    ["pychess", "Fully featured, nice looking, easy to use Chess Client", "http://www.pychess.org/"],
    ["chromium-bsu", "fast paced, arcade-style, scrolling space shooter", "http://chromium-bsu.sourceforge.net/"],
    ["woof-doom", "continuation of the Boom/MBF bloodline of Doom source ports", "https://github.com/fabiangreffrath/woof"],
    ["sauerbraten", "3D first-person shooter game", "http://sauerbraten.org/"],
    ["openarena", "fast-paced 3D first-person shooter", "https://openarena.ws/"],
    ["alien-arena", "Standalone 3D first person online deathmatch shooter", "https://martianbackup.com"],
    ["nexuiz", "Fast-paced 3D first-person shooter", "https://www.alientrap.com/games/nexuiz/"]
]

INSTALLED_TEXT, NOT_INSTALLED_TEXT, INSTALL_TEXT, REMOVE_TEXT = "yes", "no", "install", "remove"
INSTALLED_COLOR, NOT_INSTALLED_COLOR, INSTALL_COLOR, REMOVE_COLOR = "#86be43", "#c86466", "#be6cc4", "#be6cc4"
#6bb37c green
#d76c77 red
#3fa2f6 cyan
def is_installed(package_name):
    """Return True if dpkg reports the package as installed."""
    try:
        result = subprocess.run(
            ["dpkg-query", "-W", "-f=${Status}", package_name],
            capture_output=True, text=True
        )
        return result.returncode == 0 and "install ok installed" in result.stdout
    except FileNotFoundError:
        return False  # dpkg-query not available (non-Debian system)


# Store the installed boolean in softwarelist[i][3]
for item in softwarelist:
    installed = is_installed(item[0])
    if len(item) > 3:
        item[3] = installed
    else:
        item.append(installed)


class PackageTable(QTableWidget):
    """Table that emits toggle_requested when Enter or Space is pressed."""

    toggle_requested = pyqtSignal(int)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Space):
            row = self.currentRow()
            if row >= 0:
                self.toggle_requested.emit(row)
            event.accept()
            return
        super().keyPressEvent(event)


class Reiko(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("reiko")
        self.resize(700, 445)
        self.setStyleSheet("""
            QMainWindow, QWidget#central {
                background-color: #161616;
            }
            QTableWidget {
                background-color: #000000;
                color: #fecd00;
                border: none;
                gridline-color: #000000;
                selection-background-color: #3a1e3c;
                /*selection-color: #ffffff;*/
                outline: 0;
                border-bottom: 1px solid #004d66;
            }
            QTableWidget::item {
                padding: 4px;
                border: none;
            }
            QHeaderView::section {
                background-color: #222222;
                color: #eeeeee;
                border: none;
                border-bottom: 1px solid #004d66;
                padding: 4px;
                font-weight: normal;
            }
            QTableCornerButton::section {
                background-color: #040404;
                border: none;
            }
            QLabel {
                color: #eeeeee;
            }
            QPushButton {
                color: #eeeeee;
                padding: 3px 6px;
                margin: 1px 2px 1px 2px;
                background-color: #184b25;
                border: 1px solid #6bb37c;
            }
            QPushButton:hover {
                /*background-color: #27422e;
                border: 1px solid #3fa2f6;*/
            }
            QPushButton:pressed {
                margin: 2px 2px 0px 2px;
            }
            QPushButton:disabled {
                background-color: #000000;
                color: #000000;
                border: 1px solid #000000;
            }
        """)

        central = QWidget()
        central.setObjectName("central")
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        self.table = PackageTable()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["installed", "title", "description", "homepage"])
        self.table.horizontalHeader().setVisible(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        list_header = self.table.horizontalHeader()
        list_header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        list_header.setStretchLastSection(True)
        list_header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        list_header.resizeSection(0, 80)
        list_header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        list_header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        list_header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        self.table.toggle_requested.connect(self.toggle_row)
        self.table.itemDoubleClicked.connect(lambda item: self.toggle_row(item.row()))

        bottom = QHBoxLayout()
        bottom.setContentsMargins(15, 0, 6, 6)
        #bottom.setSpacing(3)

        self.counter_label = QLabel()
        self.counter_label.setFixedHeight(24)

        self.apply_button = QPushButton("Apply changes")
        self.apply_button.setFixedHeight(24)
        self.apply_button.setEnabled(False)
        self.apply_button.clicked.connect(self.apply_changes)

        bottom.addWidget(self.counter_label)
        bottom.addStretch()
        bottom.addWidget(self.apply_button)

        layout.addWidget(self.table)
        layout.addLayout(bottom)

        self.fill_table()
        self.table.setFocus()
        self.table.selectRow(0)
        self.table.setCurrentCell(0, 1)

    def fill_table(self):
        self.table.blockSignals(True)
        self.table.setRowCount(len(softwarelist))

        for row, item in enumerate(softwarelist):
            state_item = QTableWidgetItem(INSTALLED_TEXT if item[3] else NOT_INSTALLED_TEXT)
            if item[3]:
                state_item.setForeground(QColor(INSTALLED_COLOR))
            else:
                state_item.setForeground(QColor(NOT_INSTALLED_COLOR))

            state_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            state_item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

            name_item = QTableWidgetItem(item[0])
            name_item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            name_item.setForeground(QColor("#f8f8f8"))

            desc_item = QTableWidgetItem(item[1])
            desc_item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

            link_item = QTableWidgetItem(item[2])
            link_item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            link_item.setForeground(QColor("#19b9ed"))

            self.table.setItem(row, 0, state_item)
            self.table.setItem(row, 1, name_item)
            self.table.setItem(row, 2, desc_item)
            self.table.setItem(row, 3, link_item)

        self.table.blockSignals(False)

    def toggle_row(self, row):
        state_item = self.table.item(row, 0)
        if state_item.text() == INSTALLED_TEXT or state_item.text() == NOT_INSTALLED_TEXT:
            if softwarelist[row][3]:
                state_item.setText(REMOVE_TEXT)
                color = REMOVE_COLOR
            else:
                state_item.setText(INSTALL_TEXT)
                color = INSTALL_COLOR
        else:
            if softwarelist[row][3]:
                state_item.setText(INSTALLED_TEXT)
                color = INSTALLED_COLOR
            else:
                state_item.setText(NOT_INSTALLED_TEXT)
                color = NOT_INSTALLED_COLOR
        state_item.setForeground(QColor(color))
      
        """
        for col in range(self.columnCount()):
            cell = self.item(item.row(), col)
            if cell is not None:
                cell.setForeground(QColor("#00ddff"))
        """

        to_install = 0
        to_remove = 0
        for row in range(self.table.rowCount()):
            marker = self.table.item(row, 0).text()
            if marker == INSTALL_TEXT:
                to_install += 1
            elif marker == REMOVE_TEXT:
                to_remove += 1
        if to_install > 0 or to_remove > 0:
            self.counter_label.setText(f"install: {to_install}, remove: {to_remove}")
        else:
            self.counter_label.setText("")
        self.apply_button.setEnabled(to_install > 0 or to_remove > 0)

    def apply_changes(self):
        to_install = [
            softwarelist[row][0]
            for row in range(self.table.rowCount())
            if self.table.item(row, 0).text() == INSTALL_TEXT
        ]
        to_remove = [
            softwarelist[row][0]
            for row in range(self.table.rowCount())
            if self.table.item(row, 0).text() == REMOVE_TEXT
        ]

        if not to_install and not to_remove:
            return

        try:
            if to_install:
                subprocess.run(["sudo", "apt", "install", "-y", *to_install], check=True)
            if to_remove:
                subprocess.run(["sudo", "apt", "remove", "-y", *to_remove], check=True)
        except subprocess.CalledProcessError as error:
            QMessageBox.critical(self, "Error", f"apt failed: {error}")

        # Re-check the real state of every package and redraw the table
        current_row = self.table.currentRow()
        for item in softwarelist:
            item[3] = is_installed(item[0])
        self.fill_table()
        self.table.setCurrentCell(max(current_row, 0), 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Reiko()
    window.show()
    sys.exit(app.exec())
