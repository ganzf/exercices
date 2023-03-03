package ex01

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_Grumblzock(t *testing.T) {
	// Given
	orcs := 5
	// When
	result := Grumblzock(orcs)
	// Then
	if len(result) != orcs {
		t.Errorf("Expected %d, got %d", orcs, len(result))
	}
}

func Test_Grumblzock2(t *testing.T) {
	// Given
	orcs := 16
	// When
	result := Grumblzock(orcs)
	// Then
	assert.Equal(t, orcs, len(result))
	assert.Equal(t, result[0], "waagh1")
	assert.Equal(t, result[1], "waagh2")
	assert.Equal(t, result[2], "zock")
	assert.Equal(t, result[3], "waagh4")
	assert.Equal(t, result[4], "grumbl")
	assert.Equal(t, result[5], "zock")
	assert.Equal(t, result[6], "waagh7")
	assert.Equal(t, result[7], "waagh8")
	assert.Equal(t, result[8], "zock")
	assert.Equal(t, result[9], "grumbl")
	assert.Equal(t, result[10], "waagh11")
	assert.Equal(t, result[11], "zock")
	assert.Equal(t, result[12], "waagh13")
	assert.Equal(t, result[13], "waagh14")
	assert.Equal(t, result[14], "grumblzock")
	assert.Equal(t, result[15], "waagh16")
}

func Test_GrumblzockBonus(t *testing.T) {
	orcs := 70
	result := Grumblzock(orcs)
	assert.Equal(t, orcs, len(result))
	assert.Equal(t, result[68], "nice.")
}
