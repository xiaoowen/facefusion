from typing import Optional
import gradio

from facefusion import metadata

ABOUT_BUTTON : Optional[gradio.HTML] = None


def render() -> None:
	global ABOUT_BUTTON

	ABOUT_BUTTON = gradio.Button(
		value = metadata.get('name') + ' ' + metadata.get('version'),
		variant = 'primary',
	)
