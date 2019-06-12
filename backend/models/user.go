package models

type User struct {
	ID uint

	Name string
	Group *Group
}
