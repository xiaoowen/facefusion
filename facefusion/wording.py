from typing import Any, Dict, Optional

import facefusion.globals

WORDING : Dict[str, Any] =\
{
	'conda_not_activated': 'Conda is not activated',
	'python_not_supported': 'Python version is not supported, upgrade to {version} or higher',
	'ffmpeg_not_installed': 'FFMpeg is not installed',
	'creating_temp': 'Creating temporary resources',
	'extracting_frames': 'Extracting frames with a resolution of {resolution} and {fps} frames per second',
	'extracting_frames_succeed': 'Extracting frames succeed',
	'extracting_frames_failed': 'Extracting frames failed',
	'analysing': 'Analysing',
	'processing': 'Processing',
	'downloading': 'Downloading',
	'temp_frames_not_found': 'Temporary frames not found',
	'copying_image': 'Copying image with a resolution of {resolution}',
	'copying_image_succeed': 'Copying image succeed',
	'copying_image_failed': 'Copying image failed',
	'finalizing_image': 'Finalizing image with a resolution of {resolution}',
	'finalizing_image_succeed': 'Finalizing image succeed',
	'finalizing_image_skipped': 'Finalizing image skipped',
	'merging_video': 'Merging video with a resolution of {resolution} and {fps} frames per second',
	'merging_video_succeed': 'Merging video succeed',
	'merging_video_failed': 'Merging video failed',
	'skipping_audio': 'Skipping audio',
	'restoring_audio_succeed': 'Restoring audio succeed',
	'restoring_audio_skipped': 'Restoring audio skipped',
	'clearing_temp': 'Clearing temporary resources',
	'processing_stopped': 'Processing stopped',
	'processing_image_succeed': 'Processing to image succeed in {seconds} seconds',
	'processing_image_failed': 'Processing to image failed',
	'processing_video_succeed': 'Processing to video succeed in {seconds} seconds',
	'processing_video_failed': 'Processing to video failed',
	'model_download_not_done': 'Download of the model is not done',
	'model_file_not_present': 'File of the model is not present',
	'select_image_source': 'Select a image for source path',
	'select_audio_source': 'Select a audio for source path',
	'select_video_target': 'Select a video for target path',
	'select_image_or_video_target': 'Select a image or video for target path',
	'select_file_or_directory_output': 'Select a file or directory for output path',
	'no_source_face_detected': 'No source face detected',
	'frame_processor_not_loaded': 'Frame processor {frame_processor} could not be loaded',
	'frame_processor_not_implemented': 'Frame processor {frame_processor} not implemented correctly',
	'ui_layout_not_loaded': 'UI layout {ui_layout} could not be loaded',
	'ui_layout_not_implemented': 'UI layout {ui_layout} not implemented correctly',
	'stream_not_loaded': 'Stream {stream_mode} could not be loaded',
	'point': '.',
	'comma': ',',
	'colon': ':',
	'question_mark': '?',
	'exclamation_mark': '!',
	'help':
	{
		# installer
		'install_dependency': 'select the variant of {dependency} to install',
		'skip_conda': 'skip the conda environment check',
		# general
		'config': 'choose the config file to override defaults',
		'source': 'choose single or multiple source images or audios',
		'target': 'choose single target image or video',
		'output': 'specify the output file or directory',
		'listen': 'specify server listen address, default is 127.0.0.1',
		'port': 'specify server listen port, default is 7860',
		# misc
		'force_download': 'force automate downloads and exit',
		'skip_download': 'omit automate downloads and remote lookups',
		'headless': 'run the program without a user interface',
		'log_level': 'adjust the message severity displayed in the terminal',
		# execution
		'execution_device_id': 'specify the device used for processing',
		'execution_providers': 'accelerate the model inference using different providers (choices: {choices}, ...)',
		'execution_thread_count': 'specify the amount of parallel threads while processing',
		'execution_queue_count': 'specify the amount of frames each thread is processing',
		# memory
		'video_memory_strategy': 'balance fast frame processing and low VRAM usage',
		'system_memory_limit': 'limit the available RAM that can be used while processing',
		# face analyser
		'face_analyser_order': 'specify the order in which the face analyser detects faces',
		'face_analyser_age': 'filter the detected faces based on their age',
		'face_analyser_gender': 'filter the detected faces based on their gender',
		'face_detector_model': 'choose the model responsible for detecting the face',
		'face_detector_size': 'specify the size of the frame provided to the face detector',
		'face_detector_score': 'filter the detected faces base on the confidence score',
		'face_landmarker_score': 'filter the detected landmarks base on the confidence score',
		# face selector
		'face_selector_mode': 'use reference based tracking or simple matching',
		'reference_face_position': 'specify the position used to create the reference face',
		'reference_face_distance': 'specify the desired similarity between the reference face and target face',
		'reference_frame_number': 'specify the frame used to create the reference face',
		# face mask
		'face_mask_types': 'mix and match different face mask types (choices: {choices})',
		'face_mask_blur': 'specify the degree of blur applied the box mask',
		'face_mask_padding': 'apply top, right, bottom and left padding to the box mask',
		'face_mask_regions': 'choose the facial features used for the region mask (choices: {choices})',
		# frame extraction
		'trim_frame_start': 'specify the the start frame of the target video',
		'trim_frame_end': 'specify the the end frame of the target video',
		'temp_frame_format': 'specify the temporary resources format',
		'keep_temp': 'keep the temporary resources after processing',
		# output creation
		'output_image_quality': 'specify the image quality which translates to the compression factor',
		'output_image_resolution': 'specify the image output resolution based on the target image',
		'output_video_encoder': 'specify the encoder use for the video compression',
		'output_video_preset': 'balance fast video processing and video file size',
		'output_video_quality': 'specify the video quality which translates to the compression factor',
		'output_video_resolution': 'specify the video output resolution based on the target video',
		'output_video_fps': 'specify the video output fps based on the target video',
		'skip_audio': 'omit the audio from the target video',
		# frame processors
		'frame_processors': 'load a single or multiple frame processors. (choices: {choices}, ...)',
		'face_debugger_items': 'load a single or multiple frame processors (choices: {choices})',
		'face_enhancer_model': 'choose the model responsible for enhancing the face',
		'face_enhancer_blend': 'blend the enhanced into the previous face',
		'face_swapper_model': 'choose the model responsible for swapping the face',
		'frame_colorizer_model': 'choose the model responsible for colorizing the frame',
		'frame_colorizer_blend': 'blend the colorized into the previous frame',
		'frame_colorizer_size': 'specify the size of the frame provided to the frame colorizer',
		'frame_enhancer_model': 'choose the model responsible for enhancing the frame',
		'frame_enhancer_blend': 'blend the enhanced into the previous frame',
		'lip_syncer_model': 'choose the model responsible for syncing the lips',
		# uis
		'open_browser': 'open the browser once the program is ready',
		'ui_layouts': 'launch a single or multiple UI layouts (choices: {choices}, ...)'
	},
	'uis':
	{
		'en': {
			# general
			'start_button': 'START',
			'stop_button': 'STOP',
			'clear_button': 'CLEAR',
			# about
			# benchmark
			'benchmark_results_dataframe': 'BENCHMARK RESULTS',
			# benchmark options
			'benchmark_runs_checkbox_group': 'BENCHMARK RUNS',
			'benchmark_cycles_slider': 'BENCHMARK CYCLES',
			# common options
			'common_options_checkbox_group': 'OPTIONS',
			# execution
			'execution_providers_checkbox_group': 'EXECUTION PROVIDERS',
			# execution queue count
			'execution_queue_count_slider': 'EXECUTION QUEUE COUNT',
			# execution thread count
			'execution_thread_count_slider': 'EXECUTION THREAD COUNT',
			# face analyser
			'face_analyser_order_dropdown': 'FACE ANALYSER ORDER',
			'face_analyser_age_dropdown': 'FACE ANALYSER AGE',
			'face_analyser_gender_dropdown': 'FACE ANALYSER GENDER',
			'face_detector_model_dropdown': 'FACE DETECTOR MODEL',
			'face_detector_size_dropdown': 'FACE DETECTOR SIZE',
			'face_detector_score_slider': 'FACE DETECTOR SCORE',
			'face_landmarker_score_slider': 'FACE LANDMARKER SCORE',
			# face masker
			'face_mask_types_checkbox_group': 'FACE MASK TYPES',
			'face_mask_blur_slider': 'FACE MASK BLUR',
			'face_mask_padding_top_slider': 'FACE MASK PADDING TOP',
			'face_mask_padding_right_slider': 'FACE MASK PADDING RIGHT',
			'face_mask_padding_bottom_slider': 'FACE MASK PADDING BOTTOM',
			'face_mask_padding_left_slider': 'FACE MASK PADDING LEFT',
			'face_mask_region_checkbox_group': 'FACE MASK REGIONS',
			# face selector
			'face_selector_mode_dropdown': 'FACE SELECTOR MODE',
			'reference_face_gallery': 'REFERENCE FACE',
			'reference_face_distance_slider': 'REFERENCE FACE DISTANCE',
			# frame processors
			'frame_processors_checkbox_group': 'FRAME PROCESSORS',
			# frame processors options
			'face_debugger_items_checkbox_group': 'FACE DEBUGGER ITEMS',
			'face_enhancer_model_dropdown': 'FACE ENHANCER MODEL',
			'face_enhancer_blend_slider': 'FACE ENHANCER BLEND',
			'face_swapper_model_dropdown': 'FACE SWAPPER MODEL',
			'frame_colorizer_model_dropdown': 'FRAME COLORIZER MODEL',
			'frame_colorizer_blend_slider': 'FRAME COLORIZER BLEND',
			'frame_colorizer_size_dropdown': 'FRAME COLORIZER SIZE',
			'frame_enhancer_model_dropdown': 'FRAME ENHANCER MODEL',
			'frame_enhancer_blend_slider': 'FRAME ENHANCER BLEND',
			'lip_syncer_model_dropdown': 'LIP SYNCER MODEL',
			# memory
			'video_memory_strategy_dropdown': 'VIDEO MEMORY STRATEGY',
			'system_memory_limit_slider': 'SYSTEM MEMORY LIMIT',
			# output
			'output_image_or_video': 'OUTPUT',
			# output options
			'output_path_textbox': 'OUTPUT PATH',
			'output_image_quality_slider': 'OUTPUT IMAGE QUALITY',
			'output_image_resolution_dropdown': 'OUTPUT IMAGE RESOLUTION',
			'output_video_encoder_dropdown': 'OUTPUT VIDEO ENCODER',
			'output_video_preset_dropdown': 'OUTPUT VIDEO PRESET',
			'output_video_quality_slider': 'OUTPUT VIDEO QUALITY',
			'output_video_resolution_dropdown': 'OUTPUT VIDEO RESOLUTION',
			'output_video_fps_slider': 'OUTPUT VIDEO FPS',
			# preview
			'preview_image': 'PREVIEW',
			'preview_frame_slider': 'PREVIEW FRAME',
			# source
			'source_file': 'SOURCE',
			# target
			'target_file': 'TARGET',
			# temp frame
			'temp_frame_format_dropdown': 'TEMP FRAME FORMAT',
			# trim frame
			'trim_frame_start_slider': 'TRIM FRAME START',
			'trim_frame_end_slider': 'TRIM FRAME END',
			# webcam
			'webcam_image': 'WEBCAM',
			# webcam options
			'webcam_mode_radio': 'WEBCAM MODE',
			'webcam_resolution_dropdown': 'WEBCAM RESOLUTION',
			'webcam_fps_slider': 'WEBCAM FPS'
		},
		'zh_CN': {
			# general
			'start_button': '开始',
			'stop_button': '停止',
			'clear_button': '清除',
			# about
			# benchmark
			'benchmark_results_dataframe': '基准测试结果',
			# benchmark options
			'benchmark_runs_checkbox_group': '基准测试',
			'benchmark_cycles_slider': '基准周期',
			# common options
			'common_options_checkbox_group': '选项',
			# execution
			'execution_providers_checkbox_group': '执行器',
			# execution queue count
			'execution_queue_count_slider': '执行队列数',
			# execution thread count
			'execution_thread_count_slider': '执行线程数',
			# face analyser
			'face_analyser_order_dropdown': '面部分析序列',
			'face_analyser_age_dropdown': '面部分析-年龄',
			'face_analyser_gender_dropdown': '面部分析-性别',
			'face_detector_model_dropdown': '面部检测器模型',
			'face_detector_size_dropdown': '面部检测器尺寸',
			'face_detector_score_slider': '面部检测器分值',
			'face_landmarker_score_slider': '面部标记分值',
			# face masker
			'face_mask_types_checkbox_group': '面部遮罩类型',
			'face_mask_blur_slider': '面部遮罩模糊值',
			'face_mask_padding_top_slider': '面部遮罩上填充',
			'face_mask_padding_right_slider': '面部遮罩右填充',
			'face_mask_padding_bottom_slider': '面部遮罩下填充',
			'face_mask_padding_left_slider': '面部遮罩左填充',
			'face_mask_region_checkbox_group': '面部遮罩区域',
			# face selector
			'face_selector_mode_dropdown': '面部选择器模式',
			'reference_face_gallery': '面部参考',
			'reference_face_distance_slider': '面部参考值',
			# frame processors
			'frame_processors_checkbox_group': '帧处理器',
			# frame processors options
			'face_debugger_items_checkbox_group': '面部调试器',
			'face_enhancer_model_dropdown': '面部增强模型',
			'face_enhancer_blend_slider': '面部增强混淆值',
			'face_swapper_model_dropdown': '换脸模型',
			'frame_colorizer_model_dropdown': '帧着色器模型',
			'frame_colorizer_blend_slider': '帧着色器混淆值',
			'frame_colorizer_size_dropdown': '帧着色器大小',
			'frame_enhancer_model_dropdown': '帧增强模型',
			'frame_enhancer_blend_slider': '帧增强混淆值',
			'lip_syncer_model_dropdown': '唇形同步模型',
			# memory
			'video_memory_strategy_dropdown': '视频内存策略',
			'system_memory_limit_slider': '系统内存限制',
			# output
			'output_image_or_video': '输出',
			# output options
			'output_path_textbox': '输出路径',
			'output_image_quality_slider': '输出图像质量',
			'output_image_resolution_dropdown': '输出图像分辨率',
			'output_video_encoder_dropdown': '输出视频编码器',
			'output_video_preset_dropdown': '输出视频预设',
			'output_video_quality_slider': '输出视频质量',
			'output_video_resolution_dropdown': '输出视频分辨率',
			'output_video_fps_slider': '输出视频帧率',
			# preview
			'preview_image': '预览',
			'preview_frame_slider': '帧预览',
			# source
			'source_file': '源',
			# target
			'target_file': '目标',
			# temp frame
			'temp_frame_format_dropdown': '临时帧格式',
			# trim frame
			'trim_frame_start_slider': '开始修剪帧',
			'trim_frame_end_slider': '结束修剪帧',
			# webcam
			'webcam_image': '摄像头',
			# webcam options
			'webcam_mode_radio': '摄像头模式',
			'webcam_resolution_dropdown': '摄像头分辨率',
			'webcam_fps_slider': '摄像头帧率'
		}
	}
}


def get(key : str) -> Optional[str]:
	if 'uis' in key:
		section, name = key.split('.')
		if section in WORDING:
			if facefusion.globals.ui_lang in WORDING[section] and name in WORDING[section][facefusion.globals.ui_lang]:
				return WORDING[section][facefusion.globals.ui_lang][name]
			if name in WORDING[section]:
				return WORDING[section][name]
	if '.' in key:
		section, name = key.split('.')
		if section in WORDING and name in WORDING[section]:
			return WORDING[section][name]
	if key in WORDING:
		return WORDING[key]
	return None
