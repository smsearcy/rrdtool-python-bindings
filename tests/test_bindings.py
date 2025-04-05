"""Test RRDtool bindings.

Based on https://oss.oetiker.ch/rrdtool/tut/rrdtutorial.en.html

NOTE: these tests need to be run sequentially!!!

"""

from pathlib import Path

import pytest

import rrdtool

DAY = 86400
YEAR = 365 * DAY


@pytest.fixture(scope="session")
def rrd_file(tmp_path_factory) -> Path:
    """Provide pytest fixture for temporary RRD database file."""
    return tmp_path_factory.mktemp("data") / "testing.rrd"


def test_create_and_update(rrd_file) -> None:
    """Test creating RRD database."""
    assert not rrd_file.exists()
    rrdtool.create(
        str(rrd_file),
        "--start",
        "920804400",
        "DS:speed:COUNTER:600:U:U",
        "RRA:AVERAGE:0.5:1:24",
        "RRA:AVERAGE:0.5:6:10",
    )
    assert rrd_file.exists()


def test_update(rrd_file) -> None:
    """Test adding data to RRD database."""
    rrdtool.update(
        str(rrd_file), "920804700:12345", "920805000:12357", "920805300:12363"
    )
    rrdtool.update(
        str(rrd_file), "920805600:12363", "920805900:12363", "920806200:12373"
    )
    rrdtool.update(
        str(rrd_file), "920806500:12383", "920806800:12393", "920807100:12399"
    )
    rrdtool.update(
        str(rrd_file), "920807400:12405", "920807700:12411", "920808000:12415"
    )
    rrdtool.update(
        str(rrd_file), "920808300:12420", "920808600:12422", "920808900:12423"
    )


def test_dump(rrd_file: Path, tmp_path: Path) -> None:
    """Test dumping RRD database to XML."""
    rrdtool.dump(str(rrd_file), str(tmp_path / "data-dump.xml"))


def test_info(rrd_file: Path):
    """Test RRDtool info command."""
    info = rrdtool.info(str(rrd_file))
    assert isinstance(info, dict)
    assert "last_update" in info
    assert info["ds[speed].index"] == 0


def test_fetch(rrd_file: Path):
    """Test RRDtool fetch command."""
    results = rrdtool.fetch(
        str(rrd_file), "AVERAGE", "--start", "920804400", "--end", "920809200"
    )
    assert len(results) > 0
    assert "speed" in results[1]


def test_graph(rrd_file, tmp_path):
    """Test RRDtool graph command."""
    graph_filename = tmp_path / "speed.png"
    assert not graph_filename.exists()
    rrdtool.graph(
        str(graph_filename),
        "--start",
        "920804400",
        "--end",
        "920808000",
        f"DEF:myspeed={rrd_file}:speed:AVERAGE",
        "LINE2:myspeed#FF0000",
    )
    assert graph_filename.exists()


def test_graphv(rrd_file):
    """Test RRDtool graphv() function."""
    results = rrdtool.graphv(
        "-",
        "--start",
        "920804400",
        "--end",
        "920808000",
        f"DEF:myspeed={rrd_file}:speed:AVERAGE",
        "LINE2:myspeed#FF0000",
    )
    assert isinstance(results["image"], bytes)
