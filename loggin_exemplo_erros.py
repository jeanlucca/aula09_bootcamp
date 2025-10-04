from loguru import logger

logger.debug("Um aviso para o desenvolvedor( ou eu moesmo) no futuro")
logger.info("Informação importante para o processo")
logger.warning("Um aviso que algo vai parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma que aborta a aplicação")