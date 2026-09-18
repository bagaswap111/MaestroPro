import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Dialogs 1.3

/**
 * MaestroPro - MuseScore 4 Plugin
 * Maya Instruments Technology
 * "From Audio to Artistry"
 * 
 * Main UI interface for audio transcription and music analysis
 */

Rectangle {
    id: root
    
    // Branding colors
    readonly property color primaryColor: "#1a3a52"      // Deep Blue
    readonly property color accentColor: "#d4af37"       // Gold
    readonly property color backgroundColor: "#2b2b2b"   // Dark background
    readonly property color textColor: "#ffffff"         // White text
    readonly property color inputBackground: "#3c3c3c"   // Input field background
    
    width: 600
    height: 450
    
    color: backgroundColor
    
    // WebSocket connection for real-time updates
    property string websocketUrl: "ws://localhost:8765/ws/maestropro"
    property string restApiUrl: "http://localhost:8000"
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15
        
        // Header Section
        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 80
            color: primaryColor
            radius: 8
            
            ColumnLayout {
                anchors.centerIn: parent
                spacing: 5
                
                Label {
                    Layout.alignment: Qt.AlignHCenter
                    text: "🎵 MaestroPro"
                    font.pixelSize: 28
                    font.bold: true
                    color: root.textColor
                }
                
                Label {
                    Layout.alignment: Qt.AlignHCenter
                    text: "Maya Instruments Technology"
                    font.pixelSize: 12
                    color: root.accentColor
                }
                
                Label {
                    Layout.alignment: Qt.AlignHCenter
                    text: "From Audio to Artistry"
                    font.pixelSize: 11
                    font.italic: true
                    color: "#cccccc"
                }
            }
        }
        
        // YouTube URL Input Section
        GroupBox {
            Layout.fillWidth: true
            title: "Audio Source"
            font.pixelSize: 14
            font.bold: true
            
            ColumnLayout {
                anchors.fill: parent
                spacing: 10
                
                Label {
                    text: "YouTube URL or paste audio link:"
                    color: root.textColor
                    font.pixelSize: 13
                }
                
                TextField {
                    id: urlInput
                    Layout.fillWidth: true
                    placeholderText: "https://www.youtube.com/watch?v=..."
                    font.pixelSize: 14
                    
                    background: Rectangle {
                        color: root.inputBackground
                        radius: 5
                        border.color: urlInput.activeFocus ? root.accentColor : "transparent"
                        border.width: urlInput.activeFocus ? 2 : 1
                    }
                    
                    onTextChanged: {
                        if (text.length > 0) {
                            transcribeButton.enabled = true
                            transcribeButton.opacity = 1.0
                        } else {
                            transcribeButton.enabled = false
                            transcribeButton.opacity = 0.5
                        }
                    }
                }
                
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 10
                    
                    CheckBox {
                        id: separateStemsCheckbox
                        text: "Separate Stems (Vocals, Drums, Bass, Other)"
                        checked: true
                        color: root.textColor
                    }
                    
                    Item { Layout.fillWidth: true }
                    
                    ComboBox {
                        id: formatSelector
                        model: ["MusicXML", "MIDI", "Both"]
                        currentIndex: 0
                        Layout.preferredWidth: 120
                        
                        delegate: ItemDelegate {
                            width: formatSelector.width
                            contentItem: Text {
                                text: modelData
                                color: root.textColor
                                font.pixelSize: 13
                            }
                            background: Rectangle {
                                color: formatSelector.highlightedIndex === index ? root.primaryColor : root.inputBackground
                            }
                        }
                        
                        popup.background: Rectangle {
                            color: root.inputBackground
                            radius: 5
                        }
                    }
                }
            }
        }
        
        // Progress Section
        GroupBox {
            Layout.fillWidth: true
            title: "Progress"
            font.pixelSize: 14
            font.bold: true
            
            ColumnLayout {
                anchors.fill: parent
                spacing: 8
                
                ProgressBar {
                    id: progressBar
                    Layout.fillWidth: true
                    value: 0.0
                    from: 0.0
                    to: 1.0
                    
                    background: Rectangle {
                        color: root.inputBackground
                        radius: 5
                    }
                    
                    contentItem: Item {
                        implicitWidth: 200
                        implicitHeight: 20
                        
                        Rectangle {
                            width: progressBar.visualPosition * parent.width
                            height: parent.height
                            radius: 5
                            color: root.accentColor
                            
                            Behavior on width {
                                NumberAnimation { duration: 250 }
                            }
                        }
                    }
                }
                
                Label {
                    id: statusLabel
                    text: "Ready to transcribe"
                    color: "#aaaaaa"
                    font.pixelSize: 12
                    elide: Text.ElideRight
                    Layout.fillWidth: true
                }
            }
        }
        
        // Action Buttons
        RowLayout {
            Layout.fillWidth: true
            Layout.topMargin: 10
            spacing: 15
            
            Button {
                id: transcribeButton
                Layout.fillWidth: true
                Layout.preferredHeight: 45
                text: "🎼 Transcribe"
                font.pixelSize: 16
                font.bold: true
                enabled: false
                opacity: 0.5
                
                background: Rectangle {
                    color: transcribeButton.pressed ? "#0d2838" : 
                           transcribeButton.hovered ? "#255070" : root.primaryColor
                    radius: 8
                    border.color: root.accentColor
                    border.width: transcribeButton.enabled ? 2 : 0
                }
                
                contentItem: Text {
                    text: transcribeButton.text
                    color: root.textColor
                    font: transcribeButton.font
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
                
                onClicked: {
                    startTranscription()
                }
            }
            
            Button {
                id: analyzeButton
                Layout.fillWidth: true
                Layout.preferredHeight: 45
                text: "🔍 Analyze Score"
                font.pixelSize: 16
                font.bold: true
                enabled: false
                opacity: 0.5
                
                background: Rectangle {
                    color: analyzeButton.pressed ? "#0d2838" : 
                           analyzeButton.hovered ? "#255070" : root.primaryColor
                    radius: 8
                    border.color: root.accentColor
                    border.width: analyzeButton.enabled ? 2 : 0
                }
                
                contentItem: Text {
                    text: analyzeButton.text
                    color: root.textColor
                    font: analyzeButton.font
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
                
                onClicked: {
                    startAnalysis()
                }
            }
        }
        
        // Footer
        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 30
            color: "transparent"
            
            Label {
                anchors.centerIn: parent
                text: "Powered by AI • Local Processing • Privacy First"
                font.pixelSize: 10
                color: "#666666"
                font.italic: true
            }
        }
    }
    
    // Functions for backend communication
    function startTranscription() {
        if (urlInput.text.length === 0) {
            statusLabel.text = "Error: Please enter a valid URL"
            statusLabel.color = "#ff6b6b"
            return
        }
        
        statusLabel.text = "Starting transcription..."
        statusLabel.color = "#aaaaaa"
        progressBar.value = 0.1
        
        // TODO: Implement actual API call to backend
        // For now, simulate progress
        simulateTranscription()
    }
    
    function startAnalysis() {
        statusLabel.text = "Analyzing score..."
        statusLabel.color = "#aaaaaa"
        progressBar.value = 0.1
        
        // TODO: Implement actual API call to backend
        simulateAnalysis()
    }
    
    function simulateTranscription() {
        var progress = 0.1
        var interval = setInterval(function() {
            progress += 0.1
            progressBar.value = Math.min(progress, 1.0)
            
            if (progress < 0.3) {
                statusLabel.text = "Downloading audio..."
            } else if (progress < 0.5) {
                statusLabel.text = "Separating stems..."
            } else if (progress < 0.7) {
                statusLabel.text = "Transcribing to MIDI..."
            } else if (progress < 0.9) {
                statusLabel.text = "Converting to MusicXML..."
            } else if (progress >= 1.0) {
                clearInterval(interval)
                statusLabel.text = "Transcription complete! Opening in MuseScore..."
                statusLabel.color = root.accentColor
                transcribeButton.enabled = false
                
                // TODO: Open the generated MusicXML in MuseScore
            }
        }, 500)
    }
    
    function simulateAnalysis() {
        var progress = 0.1
        var interval = setInterval(function() {
            progress += 0.15
            progressBar.value = Math.min(progress, 1.0)
            
            if (progress < 0.4) {
                statusLabel.text = "Detecting key signature..."
            } else if (progress < 0.6) {
                statusLabel.text = "Analyzing chord progression..."
            } else if (progress < 0.8) {
                statusLabel.text = "Identifying musical form..."
            } else if (progress >= 1.0) {
                clearInterval(interval)
                statusLabel.text = "Analysis complete!"
                statusLabel.color = root.accentColor
            }
        }, 400)
    }
    
    Component.onCompleted: {
        console.log("MaestroPro plugin loaded")
        console.log("Maya Instruments Technology")
        // TODO: Initialize WebSocket connection
        // connectWebSocket()
    }
}
