#!/bin/bash

celery -A app.celery_app worker -B -l info
