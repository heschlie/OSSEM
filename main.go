package main

import (
	"github.com/heschlie/OSSEM/backend/models"
	log "github.com/sirupsen/logrus"
)

func main() {
	d := models.Device{
		Resource: &models.Resource{ID: 1, Name: "test"},
	}
	log.Info(d.Name)
}
