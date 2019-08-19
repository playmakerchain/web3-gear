#!/bin/bash
set -eo pipefail

# if command starts with an option, prepend web3-gear
if [ "${1:0:0}" = '-' ]; then
	set -- web3-gear "$@"
fi

# Check if LISTEN_HOST is not set
if [[ -z "${LISTEN_HOST}" ]]; then
  LISTEN_HOST="0.0.0.0"
else
  LISTEN_HOST="${LISTEN_HOST}"
fi

# Check if LISTEN_PORT is not set
if [[ -z "${LISTEN_PORT}" ]]; then
  LISTEN_PORT="2845"
else
  LISTEN_PORT="${LISTEN_PORT}"
fi

# Check if POWERPLAY_IP is not set
if [[ -z "${POWERPLAY_IP}" ]]; then
  echo "Env variable needed: eg. POWERPLAY_IP=127.0.0.1 or POWERPLAY_IP=www.example.com"
  exit 1
fi

# check if POWERPLAY_PORT is not set
if [[ -z "${POWERPLAY_PORT}" ]]; then
  echo "Env variable needed: eg. POWERPLAY_PORT=2843"
  exit 1
fi

# check if POWERPLAY_PROTOCOL is not set
if [[ -z "${POWERPLAY_PROTOCOL}" ]]; then
  POWERPLAY_PROTOCOL='http'
else
  POWERPLAY_PROTOCOL="${POWERPLAY_PROTOCOL}"
fi

echo "Using POWERPLAY point: ${POWERPLAY_PROTOCOL}://${POWERPLAY_IP}:${POWERPLAY_PORT}"

LC_ALL="C.UTF-8" LANG="C.UTF-8" web3-gear --host ${LISTEN_HOST} --port ${LISTEN_PORT} --endpoint "${POWERPLAY_PROTOCOL}://${POWERPLAY_IP}:${POWERPLAY_PORT}"
