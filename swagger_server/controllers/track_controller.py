import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.track import Track  # noqa: E501
from swagger_server import util


def add_track(body):  # noqa: E501
    """Add a new track to the database

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Track
    """
    if connexion.request.is_json:
        body = Track.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_track(track_id):  # noqa: E501
    """Deletes a track.

     # noqa: E501

    :param track_id: 
    :type track_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_track(track_id):  # noqa: E501
    """Gets a track info by idtrack

     # noqa: E501

    :param track_id: 
    :type track_id: int

    :rtype: Track
    """
    return 'do some magic!'


def update_track(body, track_id):  # noqa: E501
    """Updates a track from the database with form data.

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param track_id: 
    :type track_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Track.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
